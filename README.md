<div align="center">

# 🗳️ Registro de Miembros de Mesa

### Aplicación web que registra datos de verificación ONPE en un Excel, empaquetada en tres variantes de Docker

[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![openpyxl](https://img.shields.io/badge/openpyxl-Excel-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white)](https://openpyxl.readthedocs.io/)

</div>

---

## 📌 Sobre este proyecto

Aplicación web construida con **Flask** que registra en un archivo Excel (`.xlsx`) los datos de verificación de miembro de mesa consultados en el portal de la ONPE: DNI, región, provincia, distrito y dirección del local de votación. Desarrollada para la **Práctica Calificada 1** del curso *Desarrollo de Soluciones en la Nube* (GLAB-S04, Caso 2).

<details>
<summary><strong>🎯 Objetivo</strong> (clic para expandir)</summary>

<br>

Construir una aplicación de registro con persistencia en Excel (sin base de datos), y empaquetarla en tres variantes de Docker — comparando el resultado frente al Caso 1 para observar cómo el multi-stage build se comporta distinto según el tipo de dependencias del proyecto.

</details>

---

## ✨ Funcionalidades

| Función | Descripción |
|---|---|
| 📝 Registro | Formulario con validación de DNI (8 dígitos numéricos) |
| 📊 Persistencia | Cada envío agrega una fila a un `.xlsx` con `openpyxl` |
| 📋 Listado | Muestra todos los registros guardados en la interfaz |
| ⬇️ Descarga | Exporta el Excel completo con un clic |

---

## 🐳 Comparativa de imágenes Docker

| Dockerfile | Base | Tamaño | Estrategia |
|---|---|---|---|
| `Dockerfile` | `python:3.11-slim` | **226MB** | Instalación directa, sin dependencias de sistema |
| `Dockerfile.optimizado` | `python:3.11-alpine` | **121MB** | Base Alpine — reducción del 46% |
| `Dockerfile.multistage` | `python:3.11-alpine` (2 etapas) | **113MB** | Reducción adicional del 7% |

<details>
<summary><strong>¿Por qué la ganancia del multi-stage es tan pequeña aquí, a diferencia del Caso 1?</strong></summary>

<br>

`openpyxl` es una librería 100% Python puro — no tiene extensiones en C que compilar. Por eso la versión Alpine optimizada nunca necesitó instalar `gcc`/`musl-dev`, y el multi-stage no tuvo una etapa de build pesada que descartar. El multi-stage brilla cuando hay compilación de por medio (ver [Caso 1](../caso1)); cuando no la hay, su beneficio es marginal.

</details>

---

## 🛠️ Stack técnico

| Capa | Tecnología |
|---|---|
| Backend | Flask 3.0 (Python 3.11) |
| Persistencia | openpyxl (Excel nativo, sin base de datos) |
| Contenerización | Docker (3 variantes: base, Alpine, multi-stage) |

---

## 🚀 Correr con Docker

<details>
<summary><strong>Ver comandos</strong></summary>

<br>

```bash
# Versión base
docker build -t registro-mesa:v1.0 .

# Versión optimizada (Alpine)
docker build -f Dockerfile.optimizado -t registro-mesa:v1.1-alpine .

# Versión multi-stage
docker build -f Dockerfile.multistage -t registro-mesa:v1.2-alpine .
docker run -d -p 5002:5000 --name registro-mesa-container registro-mesa:v1.2-alpine
```

Accede en `http://localhost:5002` (o el puerto que hayas mapeado).

</details>

---

## 📂 Estructura

```
caso2/
├── app.py               # rutas Flask
├── excel_utils.py        # lógica de lectura/escritura del Excel
├── templates/
│   └── index.html
├── requirements.txt
├── Dockerfile
├── Dockerfile.optimizado
└── Dockerfile.multistage
```

---

## ✅ Checklist de la práctica

- [x] Verificación en el portal ONPE realizada
- [x] Aplicación funcional (registro + descarga de Excel)
- [x] `Dockerfile` base construido y probado
- [x] `Dockerfile.optimizado` (Alpine) construido y comparado
- [x] `Dockerfile.multistage` construido y comparado
- [x] Verificado en contenedor, corriendo en instancia EC2

---

<div align="center">

**Curso:** Desarrollo de Soluciones en la Nube · **Institución:** Tecsup
Proyecto relacionado: [Caso 1 — Descargador de Videos](../caso1)

</div>