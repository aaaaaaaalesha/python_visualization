# Python для анализа данных > Неделя 2 > Расширенная визуализация с matplotlib

from numpy.random import exponential
import matplotlib.pyplot as plt

# Создаём "холст" на котором у нас будет 2x3 = 6 графиков.
# С помощью доп. параметра figsize= мы задаём параметры в дюймах для того чтобы графики не слипались.
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(10, 5))

# Бежим по строкам. row_axes - список по колонкам.
for row, row_axes in enumerate(axes):
    # Бежим по колонкам используя row_axes. ax - текущий график, на котором мы рисуем.
    for column, ax in enumerate(row_axes):
        # Чтобы графики получались разные, зададим им начало распределение по индексу кололнки.
        ax.plot(exponential(column, 20))
        # Ставим название для каждого графика.
        ax.set_title("График. Строка {}, столбец {}".format(row + 1, column + 1))

# Данный метод делает так чтобы на одном холсте всё распределялось равномерно.
# Без наложений текста и графиков друг на друга.
fig.tight_layout()

# Сохраняем...
fig.savefig("all_results.png")

plt.show()