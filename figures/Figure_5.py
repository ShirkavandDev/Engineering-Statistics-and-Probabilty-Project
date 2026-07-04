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

df_dahak = df['Decile'].value_counts().sort_index()
fig, ax = plt.subplots(figsize=(8,5))
ax.bar(df_dahak.index, df_dahak.values, color='#55A868', edgecolor='black')
ax.set_xlabel(farsi("دهک درآمدی"))
ax.set_ylabel(farsi("تعداد افراد موجود در مجموعه داده"))
ax.set_xticks(range(1,11))

plt.savefig("images/Figure_5.png", dpi=150, bbox_inches="tight")
plt.show()
