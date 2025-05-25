import cv2
from ultralytics import YOLO
import serial
import time

# Load YOLO model
model = YOLO('best.pt')

# Connect to Arduino (change COM port as needed)
arduino = serial.Serial('COM14', 9600)
time.sleep(2)  # wait for Arduino to initialize

# Open USB webcam (usually 1 for external USB cam)
cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO detection on current frame
    results = model(frame, stream=True)

    class0_detected = False  # Flag for detecting bad class

    for r in results:
        boxes = r.boxes
        for box in boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            if conf > 0.5:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                label = model.names[cls_id]
                # Red for bad (class 0), green for good (class 1)
                color = (0, 0, 255) if cls_id == 0 else (0, 255, 0)
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

                if cls_id == 0:  # bad class detected
                    class0_detected = True

    # If bad class detected, send signal to Arduino to move servo
    if class0_detected:
        print("Bad class detected! Sending 'f' to Arduino.")
        arduino.write(b'f')
        time.sleep(2)  # delay to avoid spamming commands

    # Show detection frame
    cv2.imshow("Live Detection", frame)

    # Exit loop if 'q' pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
arduino.close()
