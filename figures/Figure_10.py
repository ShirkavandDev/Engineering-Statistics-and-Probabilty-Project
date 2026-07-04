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

urban_share = df.groupby('Decile')['isurban'].mean()*100
fig, ax = plt.subplots(figsize=(8,5))
ax.bar(urban_share.index, urban_share.values, color='#D7BA00', edgecolor='black')

ax.set_xlabel(farsi("دهک درآمدی"))
ax.set_ylabel(farsi("شهرنشینان (درصد)"))
ax.set_xticks(range(1,11))
ax.set_ylim(0,100)
plt.tight_layout()
plt.savefig("images/Figure_10.png", dpi=150, bbox_inches="tight")
plt.show()