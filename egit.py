from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(data="data.yaml",epochs=60,imgsz=640,device=0,batch=8)
