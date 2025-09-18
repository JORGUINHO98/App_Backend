# Imagen base de Python
FROM python:3.11-slim

# Establecer directorio de trabajo
WORKDIR /app

# Variables de entorno para evitar buffering y pyc
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Instalar dependencias del sistema necesarias para psycopg2 y compilación
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependencias de Python
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar el código del proyecto
COPY . /app/

# Exponer puerto de la app
EXPOSE 8050

# Comando por defecto para producción con Gunicorn
CMD ["gunicorn", "cinehub_project.wsgi:application", "--bind", "0.0.0.0:8050"]
