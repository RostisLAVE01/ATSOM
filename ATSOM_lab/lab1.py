import cv2

#2
# img1 = cv2.imread(r'D:\draw\gratis.png', cv2.IMREAD_ANYCOLOR) #Если установлено, изображение считывается в любом возможном цветовом формате.
# img2 = cv2.imread(r'D:\draw\photo3.jfif', cv2.IMREAD_REDUCED_GRAYSCALE_2) #Если установлено, всегда преобразовывать изображение
# # в одноканальное изображение в оттенках серого, а размер изображения уменьшать в два раза.
# img3 = cv2.imread(r'D:\draw\photo2.jpg', cv2.IMREAD_COLOR) #Если установлено, всегда преобразовывать изображение в 3-канальное цветное изображение BGR.
# #cv2.imshow('output', img)
# #cv2.waitKey(0)
#
# cv2.namedWindow('Display Windows 1', cv2.WINDOW_NORMAL) #пользователь может изменять размер окна (без ограничений) /
# # также использовать для переключения полноэкранного окна в обычный размер.
# cv2.imshow('Display Windows 1', img1)
# cv2.namedWindow('Display Windows 2', cv2.WINDOW_GUI_EXPANDED) #строка состояния и панель инструментов
# cv2.imshow('Display Windows 2', img2)
# cv2.namedWindow('Display Windows 3', cv2.WINDOW_KEEPRATIO) #Соотношение изображения соблюдено.
# cv2.imshow('Display Windows 3', img3)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#3
# cap = cv2.VideoCapture(r'D:\draw\video.mp4', cv2.CAP_ANY)
#
# while True:
#     ret, frame = cap.read()
#     if not(ret):
#         break
#
#     frame_resized = cv2.resize(frame, (345, 480))
#
#     frame_gray = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)
#
#     cv2.imshow('frame', frame_resized)
#     cv2.imshow('Gray', frame_gray)  # серый
#
#     #cv2.imshow('frame', frame) # изначальное
#     if cv2.waitKey(1) & 0xFF == 27:
#         break

#4
# def readIPWriteTOFile():
#     video = cv2.VideoCapture(r'D:\draw\video.mp4', cv2.CAP_ANY)
#     output = r'D:\draw\output.mp4'
#     ok, img = video.read()
#     w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
#     h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
#     fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#     video_writer = cv2.VideoWriter(output, fourcc, 25, (w, h))
#
#     while (True):
#         ok, img = video.read()
#         cv2.imshow('img', img)
#         video_writer.write(img)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#
#     video.release() # Освобождаем ресурсы
#     cv2.destroyAllWindows()
#
# readIPWriteTOFile()

#5

# img5 = cv2.imread(r'D:\draw\gratis.png')
#
# hsv = cv2.cvtColor(img5,cv2.COLOR_BGR2HSV)
#
# cv2.imshow('png',img5)
# cv2.imshow('hsv',hsv)
#
# cv2.waitKey(0)

#6

#
# def print_cam():
#     cap = cv2.VideoCapture(0)
#     cap.set(3,640)
#     cap.set(4,480)
#     while(True):
#         ret,frame = cap.read()
#     #Convert to gray scale
#         gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     #Display the resulting frame
#     cv2.imshow('frame',gray)
#     if cv2.waitKey(1) & 0xFF == 27:
#         break
#     #When everything done, release the capture
#
#     cap.release()
#     cv2.destroyAllWindows()

# def Cam():
#     video = cv2.VideoCapture(0)
#
#     if not video.isOpened():
#         print("Ошибка: Не удалось открыть камеру")
#         return
#
#     while True:
#         ok, img = video.read()
#
#         h, w, _ = img.shape # размеры
#
#         center_x, center_y = w // 2, h // 2
#
#         rect_width = 50 # Размеры прямоугольников
#         rect_height = 10
#         thickness = 2  # Толщина линии
#
#         cv2.rectangle(img, (center_x - rect_width // 2, center_y - rect_height // 2),
#                       (center_x + rect_width // 2, center_y + rect_height // 2),
#                       (0, 0, 255), thickness)
#
#         cv2.rectangle(img, (center_x - rect_height // 2, center_y - rect_width // 2),
#                       (center_x + rect_height // 2, center_y + rect_width // 2),
#                       (0, 0, 255), thickness)
#
#         cv2.imshow('Camera', img)
#
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     video.release()
#     cv2.destroyAllWindows()
#
# Cam()

#7
# def readIPWriteTOFile():
#     video = cv2.VideoCapture(0)
#     output = r'D:\draw\output.mp4'
#     ok, img = video.read()
#     w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
#     h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
#     fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#     video_writer = cv2.VideoWriter(output, fourcc, 25, (w, h))
#
#     while (True):
#         ok, img = video.read()
#         cv2.imshow('img', img)
#         video_writer.write(img)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#
#     video.release() # Освобождаем ресурсы
#     cv2.destroyAllWindows()
#
# readIPWriteTOFile()

#8

def Cam():
    video = cv2.VideoCapture(0)

    if not video.isOpened():
        print("Ошибка: Не удалось открыть камеру")
        return

    while True:
        ok, img = video.read()

        h, w, _ = img.shape # размеры

        center_x, center_y = img.shape[1] // 2, img.shape[0] // 2
        r, g, b = img[center_y, center_x]
        print(r, g, b)
        if g < r and b < r:
            color = (0, 0, 255)  # красный
        elif r < g and b < g:
            color = (0, 255, 0)  # зелёный
        else:
            color = (255, 0, 0)  # синий

        rect_width = 50 # Размеры прямоугольников
        rect_height = 10
        thickness = -1  # Толщина линии

        cv2.rectangle(img, (center_x - rect_width // 2, center_y - rect_height // 2),
                      (center_x + rect_width // 2, center_y + rect_height // 2),
                      color, thickness)

        cv2.rectangle(img, (center_x - rect_height // 2, center_y - rect_width // 2),
                      (center_x + rect_height // 2, center_y + rect_width // 2),
                      color, thickness)

        cv2.imshow('Camera', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()

Cam()

#9

# url = 'http://192.168.1.78:8080/video'
# cap = cv2.VideoCapture(url)
# while True:
#     ret, frame = cap.read()
#
#     cv2.namedWindow('Stream',cv2.WINDOW_NORMAL)
#     cv2.imshow('Stream', frame)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()

