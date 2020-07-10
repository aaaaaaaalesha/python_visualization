# Python для анализа данных > Неделя 2 > Визуализация с pandas

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")

# Гистограмма распределения по столбцу Fare.
# df.Fare.plot.hist(bins=5)

# Плотностное распределение по Fare.
# df.Fare.plot.kde()

# Распределение по нескольким значениям
# df.plot.scatter(x="Fare", y="Survived")

### Распределение по группам выживших и не выживших.(в процедурном режиме)
# 1 - график распределения выживжих.
# 2 - график распределения погибших.
# df.groupby("Survived").Fare.plot.kde()
# plt.xlim(0, 200)
# plt.legend()

### Работа в объектном режиме

## Использование объектов
# ax = df.Fare.plot.hist()
# ax.set_title("Visualisation")
# ax.figure.savefig("smth.png")


## Финалочка: распределение выживаемости по столбцу "Pclass".
fig, ax = plt.subplots(figsize=(10, 5))

df.Survived.plot.kde(label="All", ax=ax)
for label, class_df in df.groupby("Pclass"):
    print(label)
    class_df.Survived.plot.kde(ax=ax, label=label)

plt.legend()

plt.show()