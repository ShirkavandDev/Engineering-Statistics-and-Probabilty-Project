import pandas as pd
import matplotlib.pyplot as plt
import arabic_reshaper
from bidi.algorithm import get_display
import matplotlib.ticker as mticker

pd.set_option('display.max_columns', 50)
plt.rcParams['figure.dpi'] = 120

def farsi(text):
    reshaped = arabic_reshaper.reshape(text)
    return get_display(reshaped)

df = pd.read_csv("nemone_2_darsadi_1402.csv")

def millions_formatter(x, pos):
    val = x/1e6
    if val.is_integer():
        return f'{int(val)}M'
    return f'{val:.1f}M'

fig, ax = plt.subplots(figsize=(10,6))
upper = df['CardPerMonth_1402'].quantile(0.97)
data_by_decile = [df.loc[df['Decile']==d, 'CardPerMonth_1402'].dropna().clip(upper=upper) for d in range(1,11)]
bp = ax.boxplot(data_by_decile, tick_labels=[str(d) for d in range(1,11)], patch_artist=True,
                 whiskerprops=dict(color='red', linewidth=1.5, linestyle='-'),
                 capprops=dict(color='blue', linewidth=1.5),
                 boxprops=dict(facecolor='lightgray'),
                 medianprops=dict(color='black', linewidth=2))

ax.set_xlabel(farsi("دهک درآمدی"))
ax.set_ylabel(farsi("تراکنش کارت بانکی ماهانه (ریال)"))
ax.yaxis.set_major_formatter(mticker.FuncFormatter(millions_formatter))

plt.tight_layout()
plt.savefig("images/Figure_6.png", dpi=150, bbox_inches="tight")
plt.show()
