from fastapi import FastAPI, File, UploadFile, Form
from typing import List
from fastapi.middleware.cors import CORSMiddleware
import boto3
#from config.db import conn
#from schemas.Cabin import cabin

# source myenv/bin/activate
# uvicorn main:app --reload

app = FastAPI()

aws_access_key_id = 'AKIA2N337SLKYPJFIYWX'
aws_secret_access_key = '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'
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Datos de ejemplo para la lista de usuarios
users = [
    {"id": 1, "name": "Francisco cachon", "beds": 3, "price": 2500, "image": "https://sistemas-distribuidos-users.s3.amazonaws.com/cachimba.jpeg"},
    {"id": 2, "name": "Dios del fuchibol", "beds": 2, "price": 1900, "image": "https://sistemas-distribuidos-users.s3.amazonaws.com/leo-perfil-2.webp"}
]

# Endpoint para obtener la lista de usuarios
@app.get("/users")
async def get_users() -> List[dict]:
    return users

@app.post("/upload")
async def upload_image(name: str = Form(...), beds: int = Form(...), price: int = Form(...), image: UploadFile = File(...)):
    # Guardar la imagen en Amazon S3
    s3.upload_fileobj(image.file, 'sistemas-distribuidos-users', image.filename)
    url = s3.generate_presigned_url('get_object', Params={'Bucket': 'sistemas-distribuidos-users', 'Key': image.filename}, ExpiresIn=3600)
    # Persistir la cabana
    users.append({"id": users[-1]['id']+1, "name": name, "beds": beds, "price": price, "image": url})
    return {"message": "Imagen cargada correctamente"}

# @app.get("/cabins")
# async def get_cabins() -> List[dict]:
#     return conn.execute(cabin.select()).fetchall()