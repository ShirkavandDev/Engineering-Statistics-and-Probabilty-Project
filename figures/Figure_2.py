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

fig, axes = plt.subplots(1,2, figsize=(11,5))

a = df['GenderId'].value_counts().sort_index()
axes[0].bar([farsi("مرد"), farsi("زن")], a.values, color=['#4C72B0',"#F985DA"], edgecolor='black')
axes[0].set_title(farsi("توزیع جنسیت"))
axes[0].set_ylabel(farsi("تعداد"))

b = df['isurban'].value_counts(dropna=True).sort_index()
axes[1].bar([farsi("روستایی"), farsi("شهری")], b.values, color=["#B9ED84","#D7BA00"], edgecolor='black')
axes[1].set_title(farsi("توزیع شهری/روستایی"))
axes[1].set_ylabel(farsi("تعداد"))

plt.tight_layout()
plt.savefig("images/Figure_2.png", dpi=150, bbox_inches="tight")
plt.show()
