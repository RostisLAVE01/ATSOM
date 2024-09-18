import cv2
import numpy as np

#1
# def Cam():
#     cap = cv2.VideoCapture(0)
#     while(True):
#         ret,frame = cap.read()
#         hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
#         cv2.imshow('Frame', hsv)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     cap.release()
#     cv2.destroyAllWindows()
#
# Cam()


#2
# def Cam2():
#     cap = cv2.VideoCapture(0)
#
#     while True:
#         ret, frame = cap.read()
#
#         hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#
#         #диапазон красного цвета
#         lower_red1 = np.array([0, 100, 100])    # Нижний предел
#         upper_red1 = np.array([10, 255, 255])   # Верхний предел
#
#         mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
#
#         ret, red = cv2.threshold(mask1, 128, 255, cv2.THRESH_BINARY)
#
#         cv2.imshow('Camera', frame)
#         cv2.imshow('Red', red)
#
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#
#     cap.release()
#     cv2.destroyAllWindows()
#
# Cam2()


#3

# def Cam3():
#     cap = cv2.VideoCapture(0)
#
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             print("Не удалось получить кадр из камеры")
#             break
#
#         hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#
#         # Определение диапазонов для красного цвета
#         lower_red1 = np.array([0, 100, 100])  # Нижний предел
#         upper_red1 = np.array([10, 255, 255])  # Верхний предел
#
#         mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
#
#         ret, red = cv2.threshold(mask1, 128, 255, cv2.THRESH_BINARY)
#
#         kernel = np.ones((3, 3), np.uint8)
#         opening = cv2.morphologyEx(red, cv2.MORPH_OPEN, kernel)  # Открытие
#         closing = cv2.morphologyEx(red, cv2.MORPH_CLOSE, kernel)  # Закрытие
#
#         cv2.imshow('Camera', frame)
#         cv2.imshow('Open', opening)
#         cv2.imshow('Close', closing)
#
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#
#     cap.release()
#     cv2.destroyAllWindows()
#
#
# Cam3()

#4 что такое изображение первого порядка !!!!

# def Cam4():
#     cap = cv2.VideoCapture(0)
#
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             print("Не удалось получить кадр из камеры")
#             break
#
#         hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#
#         # Определение диапазонов для красного цвета
#         lower_red1 = np.array([0, 100, 100])  # Нижний предел
#         upper_red1 = np.array([10, 255, 255])  # Верхний предел
#
#         mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
#
#         ret, red = cv2.threshold(mask1, 128, 255, cv2.THRESH_BINARY)
#
#         moment = cv2.moments(red)
#
#         square = moment['m00'] # площадь
#         print(f"Площадь объекта: {square}")
#
#
#         cv2.imshow('Camera', frame)
#
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#
#     cap.release()
#     cv2.destroyAllWindows()
#
#
# Cam4()

#5

def Cam5():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Не удалось получить кадр из камеры")
            break

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Определение диапазонов для красного цвета
        lower_red1 = np.array([0, 100, 100])  # Нижний предел
        upper_red1 = np.array([10, 255, 255])  # Верхний предел

        mask1 = cv2.inRange(hsv, lower_red1, upper_red1)

        ret, red = cv2.threshold(mask1, 128, 255, cv2.THRESH_BINARY)

        cont, _ = cv2.findContours(red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for con in cont:

            moment = cv2.moments(con)
            square = moment['m00']  # площадь

            if square != 0:
                centerX = int(moment['m10'] / square)
                centerY = int(moment['m01'] / square)
            else:
                centerX, centerY = 0, 0

            print(f"центр по х: {centerX}")
            print(f"центр по у: {centerY}")



            x, y, w, h = cv2.boundingRect(con)

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 2)


        cv2.imshow('Camera', frame)
        cv2.imshow('RED', red)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


Cam5()

