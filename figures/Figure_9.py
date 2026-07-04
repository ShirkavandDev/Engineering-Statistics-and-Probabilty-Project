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

df['HasCar'] = (df['CarsCount'].fillna(0) > 0).astype(int)
fig, axes = plt.subplots(1,2, figsize=(12,5))
car_own = df.groupby('Decile')['HasCar'].mean()*100
axes[0].bar(car_own.index, car_own.values, color='#55A868', edgecolor='black')
axes[0].set_title(farsi("تملک خودرو"))
axes[0].set_xlabel(farsi("دهک درآمدی"))
axes[0].set_ylabel(farsi("نرخ تملک خودرو (درصد)"))
axes[0].set_xticks(range(1,11))

govt = df.groupby('Decile')['ISKarmanddolat_1402'].mean()*100
axes[1].bar(govt.index, govt.values, color='#4C72B0', edgecolor='black')
axes[1].set_title(farsi("اشتغال دولتی"))
axes[1].set_xlabel(farsi("دهک درآمدی"))
axes[1].set_ylabel(farsi("تعداد کارمندان دولت (درصد)"))
axes[1].set_xticks(range(1,11))
plt.tight_layout()
plt.savefig("images/Figure_9.png", dpi=150, bbox_inches="tight")
plt.show()