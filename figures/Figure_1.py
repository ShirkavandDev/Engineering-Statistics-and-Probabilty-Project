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

fig, ax = plt.subplots(figsize=(8,5))
ax.hist(df['Age'].dropna(), bins=30, color="#3B71E7", edgecolor='black')
ax.set_xlabel(farsi("سن (سال)"))
ax.set_ylabel(farsi("فراوانی"))
plt.savefig("images/Figure_1.png", dpi=150, bbox_inches="tight")
plt.show()
