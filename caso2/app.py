from flask import Flask, flash, redirect, render_template, request, send_file, url_for

from excel_utils import EXCEL_PATH, agregar_registro, listar_registros

app = Flask(__name__)
app.secret_key = "clave-de-desarrollo-cambia-en-produccion"


@app.route("/")
def index():
    return render_template("index.html", registros=listar_registros())


@app.route("/registrar", methods=["POST"])
def registrar():
    dni = request.form.get("dni", "").strip()
    region = request.form.get("region", "").strip()
    provincia = request.form.get("provincia", "").strip()
    distrito = request.form.get("distrito", "").strip()
    direccion = request.form.get("direccion", "").strip()

    if not dni or len(dni) != 8 or not dni.isdigit():
        flash("El DNI debe tener exactamente 8 dígitos numéricos.", "error")
        return redirect(url_for("index"))

    if not all([region, provincia, distrito, direccion]):
        flash("Todos los campos son obligatorios.", "error")
        return redirect(url_for("index"))

    agregar_registro(dni, region, provincia, distrito, direccion)
    flash("Registro agregado correctamente.", "success")
    return redirect(url_for("index"))


@app.route("/descargar")
def descargar():
    return send_file(EXCEL_PATH, as_attachment=True, download_name="miembros_mesa.xlsx")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)