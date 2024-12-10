import keras
import numpy as np
import matplotlib.pyplot as plt
from keras._tf_keras.keras.datasets import mnist
from keras._tf_keras.keras.models import Sequential
from keras._tf_keras.keras.layers import Dense, Flatten
from keras._tf_keras.keras.utils import to_categorical
from keras.src.layers import Conv2D, MaxPooling2D

# Загрузка данных
(x_train, y_train), (x_test, y_test) = mnist.load_data()

num_classes = 10

x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
input_shape = (28,28,1)

y_train = to_categorical(y_train, num_classes)         # Преобразование меток в one-hot
y_test = to_categorical(y_test, num_classes)           # Преобразование меток в one-hot

# Предобработка данных
x_train = x_train.astype('float32') # Нормализация
x_test = x_test.astype('float32')   # Нормализация

x_train /= 255.0
x_test /= 255.0

batch_size = 16
epochs = 1

# Создание модели
model = Sequential()

model.add(Conv2D(32, kernel_size = (3,3), activation = 'relu', input_shape = input_shape, padding = 'same'))
model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Conv2D(64, kernel_size = (3,3), activation = 'relu', padding = 'same'))
model.add(Flatten())
model.add(Dense(256, activation='relu'))      # Скрытый слой с 128 нейронами
model.add(Dense(64, activation='relu'))       # Еще один скрытый слой с 64 нейронами
model.add(Dense(num_classes, activation='softmax'))
model.compile(loss= keras.losses.categorical_crossentropy,
              optimizer='adam',
              metrics=['accuracy'])


# Обучение модели
model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size, validation_data=(x_test, y_test))

# Оценка модели
loss, accuracy = model.evaluate(x_test, y_test)
print(f'Потери при тестировании: {loss:.4f}, точность теста: {accuracy:.4f}')

# Предсказание на тестовых данных
predictions = model.predict(x_test)

# Визуализация результатов
for i in range(10):
    plt.imshow(x_test[i], cmap='gray')
    plt.title(f'Ожидаемое: {np.argmax(y_test[i])}, Результат: {np.argmax(predictions[i])}')
    plt.show()