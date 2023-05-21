# Define la imagen base
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# Copia el código de tu aplicación a la carpeta /app dentro del contenedor
COPY ./main.py /app/main.py

# Instala las dependencias de tu aplicación
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Expone el puerto 80 para que el contenedor escuche las solicitudes entrantes
EXPOSE 80

# Comando para iniciar la aplicación cuando se ejecute el contenedor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
