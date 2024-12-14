import cv2
import pytesseract
import easyocr
import os
import json
from PIL import Image
import pandas as pd

pytesseract.pytesseract.tesseract_cmd = (r"D:\draw\tesseract\tesseract.exe")

# img = cv2.imread('D:\\draw\\yandex-capchi\\2-.jpg')
# cv2.imshow('Image', img)
# text = pytesseract.image_to_string(img, lang='rus+eng')
# print(text)
# cv2.waitKey(0)


def load_annotations(annotations_file):
    annotations = {}
    with open(annotations_file, 'r', encoding='utf-8') as f:
        for line in f:
            filename, true_text = line.strip().split('|')
            annotations[filename.strip()] = true_text.strip()
    return annotations


def test_recognition(annotations):
    results = []
    for filename, true_text in annotations.items():
        if not os.path.exists(filename):
            print(f'Файл {filename} не найден!')
            continue
        image = Image.open(filename)
        recognized_text = pytesseract.image_to_string(image)
        match = recognized_text.strip() == true_text.strip()
        results.append({
            'filename': filename,
            'recognized': recognized_text.strip(),
            'true': true_text.strip(),
            'match': match
        })
    results_df = pd.DataFrame(results)
    print(f'Обработано изображений: {len(results_df)}, Найдено совпадений: {results_df["match"].sum()}')  # Для отладки
    return results_df


annotations_file = 'D:\\draw\\annotations.txt'
original_annotations = load_annotations(annotations_file)
results_df = test_recognition(original_annotations)

# Сохранение результатов
results_df.to_csv('original_results.csv', index=False, encoding='utf-8')


def augment_dataset(annotations, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    augmentations = []

    for filename, true_text in annotations.items():
        if not os.path.exists(filename):
            print(f'Файл {filename} не найден для аугментации!')
            continue
        image = Image.open(filename)
        for angle in range(-20, 21):  # от -20 до 20 включая
            rotated_image = image.rotate(angle)
            rotated_filename = f"{os.path.splitext(os.path.basename(filename))[0]}_rot{angle}.jpg"
            rotated_image.save(os.path.join(output_dir, rotated_filename))
            augmentations.append((os.path.join(output_dir, rotated_filename), true_text))

    # Вывести все файлы в директории
    print(f'Всего аугментированных файлов: {len(augmentations)}')
    return augmentations


output_dir = 'augmented_dataset'
augmented_annotations = augment_dataset(original_annotations, output_dir)

# Тестирование аугментированных изображений
augmented_df = test_recognition({filename: true_text for filename, true_text in augmented_annotations})
# Сохранение результатов аугментированной проверки
augmented_df.to_csv('augmented_results.csv', index=False, encoding='utf-8')

# Сводная таблица
summary_df = pd.DataFrame({
    'Original Total': [len(original_annotations)],
    'Original Correct': [results_df['match'].sum()],
    'Original Accuracy': [results_df['match'].mean() * 100],
    'Augmented Total': [len(augmented_annotations)],
    'Augmented Correct': [augmented_df['match'].sum() if 'match' in augmented_df.columns else 0],
    'Augmented Accuracy': [augmented_df['match'].mean() * 100 if 'match' in augmented_df.columns else 0]
})

summary_df.to_csv('summary_results.csv', index=False, encoding='utf-8')

