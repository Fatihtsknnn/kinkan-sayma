from fastapi import FastAPI, File, UploadFile
from ultralytics import YOLO
from PIL import Image 
import  numpy as np 
import io 

app = FastAPI()
model = YOLO("model.pt")

@app.get ("/")
def merhaba():
    return {"mesaj": "API CALİSİYOR..."}

@app.post ("/tahmin")
async def tahmin(file: UploadFile = File(...)):
    icerik = await file.read() 
    resim = Image.open(io.BytesIO(icerik)).convert("RGB") 
    resim_np = np.array(resim)
    r = model(resim_np)[0]
    sayi = len(r.boxes)
    return {"kinkan_sayisi": sayi}