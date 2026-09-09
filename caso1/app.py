import os
import uuid

from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    send_from_directory,
    request,
    url_for,
)
from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "clave-de-desarrollo-cambia-en-produccion")

DOWNLOAD_DIR = os.path.join(os.path.dirname(__file__), "downloads")
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Redes soportadas mostradas en la interfaz (yt-dlp soporta muchas más internamente)
REDES_SOPORTADAS = ["YouTube", "TikTok", "Instagram", "Facebook", "LinkedIn"]


def listar_descargas():
    """Devuelve los archivos ya descargados, más recientes primero."""
    archivos = [
        f
        for f in os.listdir(DOWNLOAD_DIR)
        if os.path.isfile(os.path.join(DOWNLOAD_DIR, f)) and not f.startswith(".")
    ]
    archivos.sort(
        key=lambda f: os.path.getmtime(os.path.join(DOWNLOAD_DIR, f)), reverse=True
    )
    return archivos


@app.route("/")
def index():
    return render_template(
        "index.html", redes=REDES_SOPORTADAS, descargas=listar_descargas()
    )


@app.route("/download", methods=["POST"])
def download():
    url = request.form.get("url", "").strip()
    calidad = request.form.get("calidad", "video")

    if not url:
        flash("Ingresa una URL válida.", "error")
        return redirect(url_for("index"))

    # Nombre de archivo único para evitar colisiones entre descargas
    nombre_base = str(uuid.uuid4())[:8]

    if calidad == "audio":
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": os.path.join(DOWNLOAD_DIR, f"{nombre_base}-%(title)s.%(ext)s"),
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
            "noplaylist": True,
        }
    else:
        ydl_opts = {
            "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
            "outtmpl": os.path.join(DOWNLOAD_DIR, f"{nombre_base}-%(title)s.%(ext)s"),
            "noplaylist": True,
        }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        flash("Descarga completada correctamente.", "success")
    except DownloadError as exc:
        flash(f"No se pudo descargar el video: {exc}", "error")
    except Exception as exc:  # noqa: BLE001 - mostramos cualquier error al usuario
        flash(f"Error inesperado: {exc}", "error")

    return redirect(url_for("index"))


@app.route("/archivos/<path:nombre_archivo>")
def servir_archivo(nombre_archivo):
    return send_from_directory(DOWNLOAD_DIR, nombre_archivo, as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
