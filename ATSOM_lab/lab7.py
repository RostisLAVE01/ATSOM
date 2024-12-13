import cv2
import pytesseract
import easyocr
import os
import json
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = (r"D:\draw\tesseract\tesseract.exe")

# img = cv2.imread('D:\\draw\\yandex-capchi\\2-.jpg')
# cv2.imshow('Image', img)
# text = pytesseract.image_to_string(img, lang='rus+eng')
# print(text)
# cv2.waitKey(0)



def test_recognition(rec_type, val_type, annotations_file):
    # Загружаем аннотации
    annotations = {}
    with open(annotations_file, 'r', encoding='utf-8') as f:
        for line in f:
            filename, true_text = line.strip().split('|')
            annotations[filename] = true_text

    results = []

    for filename, true_text in annotations.items():
        # Проверяем, существует ли изображение
        if not os.path.exists(filename):
            print(f'Файл {filename} не найден!')
            continue

        # Загружаем изображение
        image = Image.open(filename)

        if rec_type == 'tesseract':
            recognized_text = pytesseract.image_to_string(image)
            print(f'Распознанный текст: {recognized_text.strip()} для изображения: {filename}')
            print(f'Ожидаемый текст: {true_text.strip()} для изображения: {filename}')
        elif rec_type == 'easyocr':
            reader = easyocr.Reader(['en'])
            results_easyocr = reader.readtext(filename)
            recognized_text = ' '.join([result[1] for result in results_easyocr])
        else:
            raise ValueError(f'Неподдерживаемый тип распознавания: {rec_type}')

        # Оценка качества распознавания
        if val_type == 'exact':
            match = recognized_text.strip() == true_text.strip()
        elif val_type == 'partial':
            match = true_text.strip() in recognized_text.strip()
        else:
            raise ValueError(f'Неподдерживаемый тип оценки валидности: {val_type}')

        results.append((recognized_text.strip(), true_text.strip(), match))

    # Запись результатов в файл
    with open('recognition_results.txt', 'w', encoding='utf-8') as f:
        for recognized, true, match in results:
            f.write(f'{recognized}|{true}|{match}\n')

    # Подсчет статистики
    total = len(results)
    correct = sum(1 for r in results if r[2])
    accuracy = correct / total if total > 0 else 0

    return {
        'total': total,
        'correct': correct,
        'accuracy': accuracy
    }



rec_type = 'tesseract'  # Или 'easyocr'
val_type = 'exact'  # Или 'partial'
annotations_file = 'D:\\draw\\annotations.txt'

stats = test_recognition(rec_type, val_type, annotations_file)
print(f"Всего: {stats['total']}, Верно: {stats['correct']}, Точность: {stats['accuracy']:.2%}")
