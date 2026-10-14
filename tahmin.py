from ultralytics import YOLO

model = YOLO("runs/detect/train/weights/best.pt")
r = model("test/images/IMG_2037_JPG_jpg.rf.b4ae60ea91f6e1db621a2f7ab9a43aa9.jpg")[0]
sayi = len(r.boxes)
r.save("sonuc.jpg")

print(f"Bu görselde {sayi} kinkan var")
