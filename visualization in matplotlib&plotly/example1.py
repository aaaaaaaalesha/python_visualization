# Python для анализа данных > Неделя 2 > Визуализация  matplotlib

import matplotlib.pyplot as plt
from numpy.random import exponential

# Создаём датасеты с экспоненциальным распределением
data1 = exponential(5, 20)
data2 = exponential(6, 20)

# Создаём график по датасету1 фиолетового цвета и лейблом для создания легенды.
plt.plot(data1, color='purple', label="Первый игрок")

# scatter - задание графика точками.
plt.scatter(range(len(data2)), data2, color='red', label="Второй игрок")

# Название.
plt.title("Результаты", fontdict={'fontsize': 20})

# Подпись оси x.
plt.xlabel("Номер попытки")

# Подпись оси y.
plt.ylabel("Результат")

# Легенда (только если указаны параметры label при создании plt.plot(...)
plt.legend()

# Задаём шаг отметок на оси X.(масштаб в каком-то смысле)
plt.xticks(range(0, 20, 4))

# Сохранить график(и) в файл с заданным расширением.
plt.savefig('results.pdf')

plt.show()