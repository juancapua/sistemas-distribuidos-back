from fastapi import FastAPI, File, UploadFile, Form
from typing import List
from fastapi.middleware.cors import CORSMiddleware
import boto3
from config.db import conn
from schemas.Cabin import cabin

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

@app.get("/cabins")
async def get_cabins() -> List[dict]:
    return conn.execute(cabin.select()).fetchall()

@app.post("/upload")
async def upload_cabin(name: str = Form(...), beds: int = Form(...), price: int = Form(...), image: UploadFile = File(...)):
    # Guardar la imagen en Amazon S3
    s3.upload_fileobj(image.file, 'sistemas-distribuidos-users', image.filename)
    url = s3.generate_presigned_url('get_object', Params={'Bucket': 'sistemas-distribuidos-users', 'Key': image.filename}, ExpiresIn=3600)
    new_cabin = {"name": name, "beds": beds, "price": price, "image": url}
    conn.execute(cabin.insert().values(new_cabin))

    return {"message": "Cabaña agregada correctamente"}