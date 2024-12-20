import cv2
from ultralytics import YOLO

#
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#
#
# cap = cv2.VideoCapture(0)
#
# while True:
#
#     ret, frame = cap.read()
#     if not ret:
#         break
#
#
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
#
#
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
#
#
#     cv2.imshow('Video', frame)
#
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
#
# cap.release()
# cv2.destroyAllWindows()


model = YOLO('yolov8n.pt')
model.conf = 0.2


cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break


    results = model(frame)


    for result in results:

        for box in result.boxes:
             # Получение координат, уверенности и класса
            x1, y1, x2, y2 = box.xyxy[0]  # Координаты
            conf = box.conf[0]  # Уверенность
            cls = int(box.cls[0])  # Класс


            if cls == 0:

                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                cv2.putText(frame, f'Confidence: {conf:.2f}', (int(x1), int(y1) - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


    processed_frame = frame

    cv2.imshow('Real-time Face Detection', processed_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
