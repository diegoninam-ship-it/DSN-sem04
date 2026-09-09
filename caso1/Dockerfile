# Imagen base - Python oficial
FROM python:3.11-slim

# Metadata
LABEL maintainer="diego@ejemplo.com"
LABEL description="Descargador de videos multi-red (YouTube, TikTok, Instagram, Facebook, LinkedIn)"

# Instalar ffmpeg — necesario para que yt-dlp una video+audio o extraiga MP3
RUN apt-get update && apt-get install -y --no-install-recommends ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivo de dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código de la aplicación
COPY app.py .
COPY templates/ templates/

# Exponer el puerto
EXPOSE 5000

# Comando por defecto
CMD ["python", "app.py"]