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

#4

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
#         centerX = int(moment['m10'] / square)
#         centerY = int(moment['m01'] / square)
#
#         print(f"центр по х: {centerX}")
#         print(f"центр по у: {centerY}")
#
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
def conters(frame):
    marked = np.zeros(frame.shape, dtype=bool)
    cont = []

    for x in range(frame.shape[0]):
        for y in range(frame.shape[1]):
            if frame[x, y] == 255 and not marked[x, y]:
                start = [(x, y)] #начальное значение
                comp = []

                while start:
                    current = start.pop()
                    if not marked[current]:
                        marked[current] = True
                        comp.append(current)
                        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nx, ny = current[0] + dx, current[1] + dy
                            if (0 <= nx < frame.shape[0] and
                                    0 <= ny < frame.shape[1] and
                                    frame[nx, ny] == 255 and
                                    not marked[nx, ny]):
                                start.append((nx, ny))
                cont.append(comp)

    return cont

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

        kernel = np.ones((7, 7), np.uint8)
        closing = cv2.morphologyEx(red, cv2.MORPH_CLOSE, kernel)
        cont = conters(closing)


        for con in cont:

            con_mas = np.array(con)
            x, y, w, h = cv2.boundingRect(con_mas.reshape(-1, 1, 2))

            cv2.rectangle(frame, (y, x), (y + w, x + h), (255, 0, 0), 2)


        cv2.imshow('Camera', frame)
        cv2.imshow('RED', red)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()



