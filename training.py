from ultralytics import YOLO


model=YOLO("yolov8n.pt")

results = model.train(
    data="./dataset/dataset.yaml",
    epochs=100,
    imgsz=640,
    device="cpu",
    workers=2,
)
print("AI TRAINING COMPLETE!")