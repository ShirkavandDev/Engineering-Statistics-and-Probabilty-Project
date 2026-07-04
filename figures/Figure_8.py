import pandas as pd
import matplotlib.pyplot as plt
import arabic_reshaper
from bidi.algorithm import get_display
from scipy.stats import spearmanr

pd.set_option('display.max_columns', 50)
plt.rcParams['figure.dpi'] = 120

def farsi(text):
    reshaped = arabic_reshaper.reshape(text)
    return get_display(reshaped)

df = pd.read_csv("nemone_2_darsadi_1402.csv")

df['GenderFemale'] = (df['GenderId'] == 2).astype(int)

names = [
    'سن',
    'جنسیت (زن)',
    'شهرنشین',
    'ارزش سبد سهام',
    'جواز کسب',
    'کارمند دولت',
    'بیماری خاص',
    'معلولیت',
    'سوء تغذیه',
    'بازنشسته اصلی',
    'بازنشسته تبعی',
    'بیمه پرداز'
]

cols = [
    'Age',
    'GenderFemale',
    'isurban',
    'Bourse_NetPortfoValue',
    'HasMojavezSenfi',
    'ISKarmanddolat_1402',
    'ISBimarKhas',
    'IsMalool',
    'Has_SoeTaghzie',
    'IsRetired_Asli',
    'IsRetired_Tabaie',
    'IsBimePardaz'
]

binary = [
    'ISBimarKhas',
    'IsMalool',
    'Has_SoeTaghzie',
    'Has_Saham_Edalat',
    'HasMojavezSenfi',
    'ISKarmanddolat_1402',
    'IsRetired_Asli',
    'IsRetired_Tabaie',
    'IsBimePardaz'
]

for i in binary:
    df[i] = df[i].fillna(0)

corr = []

for i in cols:
    data = df[['Decile', i]].dropna()
    r, p = spearmanr(data['Decile'], data[i])
    corr.append(r)

table = pd.DataFrame()
table['نام'] = names
table['همبستگی'] = corr

table = table.sort_values('همبستگی')
table = table.reset_index(drop=True)

colors = []

for i in table['همبستگی']:
    if i >= 0:
        colors.append('green')
    else:
        colors.append('red')

labels = []

for i in table['نام']:
    labels.append(farsi(i))

plt.figure(figsize=(15, 8))

plt.barh(labels, table['همبستگی'], color=colors, edgecolor='black')

for i in range(len(table)):
    value = table.loc[i, 'همبستگی']

    if value >= 0:
        plt.text(value + 0.005, i, str(round(value, 3)),
                 va='center', fontsize=9)
    else:
        plt.text(value - 0.005, i, str(round(value, 3)),
                 va='center', ha='right', fontsize=9)

plt.xlabel(farsi("مقدار همبستگی با درآمد (اسپیرمن)"))

plt.tight_layout()
plt.savefig("images/Figure_8.png", dpi=150, bbox_inches="tight")
plt.show()