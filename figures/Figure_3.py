import pandas as pd
import matplotlib.pyplot as plt
import arabic_reshaper
from bidi.algorithm import get_display

pd.set_option('display.max_columns', 50)
plt.rcParams['figure.dpi'] = 120

def farsi(text):
    reshaped = arabic_reshaper.reshape(text)
    return get_display(reshaped)

df = pd.read_csv("nemone_2_darsadi_1402.csv")

fig, ax = plt.subplots(figsize=(10,6))

population = df['SabteAhval_provincename'].value_counts().head(10)

city_names = []
for city in population.index[::-1]:
    city_names.append(farsi(city))

ax.barh(city_names, population.values[::-1], color="#D25054", edgecolor='black')
ax.set_xlabel(farsi("تعداد ساکنین موجود در مجموعه داده"))

plt.savefig("images/Figure_3.png", dpi=150, bbox_inches="tight")
plt.show()
