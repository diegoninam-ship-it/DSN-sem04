# Imagen base - Python oficial
FROM python:3.11-slim

# Metadata
LABEL maintainer="diego@ejemplo.com"
LABEL description="Registro de miembros de mesa - consulta ONPE"

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivo de dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código de la aplicación
COPY app.py excel_utils.py .
COPY templates/ templates/

# Exponer el puerto
EXPOSE 5000

# Comando por defecto
CMD ["python", "app.py"]