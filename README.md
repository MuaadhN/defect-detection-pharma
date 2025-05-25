# Defect Detection in Pharmaceutical Packaging using YOLO

A real-time defect detection system using YOLOv11m for identifying packaging defects in pharmaceutical boxes on a conveyor belt, integrated with servo-based actuation.

## 🔍 Features
- YOLO-based object detection
- Custom dataset collection and augmentation
- Real-time servo control with Arduino
- 96% mAP@50 with YOLOv11m

## 📂 Folder Structure
- `notebooks/`: Model training and evaluation
- `deployment/`: Arduino and hardware code
- `data/`: Sample images
- `app.py`: Live detection script

## 🚀 Run Inference
```bash
python app.py --model app.pt
