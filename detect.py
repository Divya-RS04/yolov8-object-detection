from ultralytics import YOLO
import os

# Set save directory to your project folder
save_path = r"D:\PROJECTS\yolov8_object_detection"

# Load model
model = YOLO("yolov8n.pt")

# Run detection and force save location
results = model(
    "bus.jpg",
    save=True,
    project=save_path,
    name="result.jpg"
)

print("Detection completed. Check the D folder!")

