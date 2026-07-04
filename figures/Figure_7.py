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

card_cols = ['CardPerMonth_1398','CardPerMonth_1399','CardPerMonth_1400',
             'CardPerMonth_1401','CardPerMonth_1402']
years = ['1398','1399','1400','1401','1402']
# AI is used here
# AI use is explicitly mentioned in report.pdf
# ================================================================
# INFLATION ADJUSTMENT — Central Bank of Iran (CBI), cbi.ir
# Annual CPI rates, March-to-March (= one Persian Solar year)
# Source: https://cbi.ir/Inflation/Inflation_en.aspx
# ================================================================
inflation_rates = {
    1398: 41.2,   # March 2019 – March 2020
    1399: 47.1,   # March 2020 – March 2021
    1400: 46.2,   # March 2021 – March 2022
    1401: 53.1,   # March 2022 – March 2023
    1402: 47.4,   # March 2023 – March 2024
}

# Cumulative price index, base year 1398 = 1.0
cpi = {1398: 1.0}
for y in [1399, 1400, 1401, 1402]:
    cpi[y] = cpi[y-1] * (1 + inflation_rates[y] / 100)

print("=== CPI deflators (base = 1398) ===")
for y, factor in cpi.items():
    print(f"  {y}: {factor:.4f}  (prices are {factor:.2f}× the 1398 level)")

total_cum = (cpi[1402] - 1) * 100

card_cols  = ['CardPerMonth_1398','CardPerMonth_1399','CardPerMonth_1400',
              'CardPerMonth_1401','CardPerMonth_1402']
years_int  = [1398, 1399, 1400, 1401, 1402]
for col, y in zip(card_cols, years_int):
    df[f'Real_{col}'] = df[col] / cpi[y]

real_cols = [f'Real_{c}' for c in card_cols]

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

upper_nominal = df[card_cols].quantile(0.97).max()
upper_real    = df[real_cols].quantile(0.97).max()

data_nominal = [df[c].dropna().clip(upper=upper_nominal) for c in card_cols]
axes[0].boxplot(data_nominal, tick_labels=years, patch_artist=True,
                whiskerprops=dict(color='red', linewidth=1.5, linestyle='-'),
                capprops=dict(color='blue', linewidth=1.5),
                boxprops=dict(facecolor='lightgray'),
                medianprops=dict(color='black', linewidth=2),
                showfliers=False)
axes[0].set_title(farsi("با اثر تورم"), fontsize=11)
axes[0].set_xlabel(farsi("سال"))
axes[0].set_ylabel(farsi("تراکنش ماهانه کارت بانکی (ریال)"))
axes[0].yaxis.set_major_formatter(mticker.FuncFormatter(millions_formatter))

data_real = [df[c].dropna().clip(upper=upper_real) for c in real_cols]
axes[1].boxplot(data_real, tick_labels=years, patch_artist=True,
                whiskerprops=dict(color='red', linewidth=1.5, linestyle='-'),
                capprops=dict(color='blue', linewidth=1.5),
                boxprops=dict(facecolor='#B3D9FF'),
                medianprops=dict(color='black', linewidth=2),
                showfliers=False)
axes[1].set_title(farsi("با حذف اثر تورم"), fontsize=11)
axes[1].set_xlabel(farsi("سال"))
axes[1].set_ylabel(farsi("تراکنش ماهانه کارت بانکی (با ارزش پول 1398)"))
axes[1].yaxis.set_major_formatter(mticker.FuncFormatter(millions_formatter))

plt.tight_layout()
plt.savefig("images/Figure_7.png", dpi=150, bbox_inches="tight")
plt.show()