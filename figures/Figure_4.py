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

df['AgeGroup'] = pd.cut(df['Age'], bins=[0,10,20,30,40,50,60,70,80,100], labels=['0-10','11-20','21-30','31-40','41-50','51-60','61-70','71-80','80+'])

male = df[df['GenderId'] == 1]
female = df[df['GenderId'] == 2]

male_avg = male.groupby('AgeGroup')['CardPerMonth_1402'].mean()
female_avg = female.groupby('AgeGroup')['CardPerMonth_1402'].mean()

plt.figure(figsize=(10,5))
plt.plot(male_avg.index.astype(str), male_avg.values / 1000000, label=farsi("مرد"))
plt.plot(female_avg.index.astype(str), female_avg.values / 1000000, label=farsi("زن"))

plt.xlabel(farsi("سن (سال)"))
plt.ylabel(farsi("میانگین تراکنش بانکی (میلیون ریال)"))
plt.legend()

plt.savefig("images/Figure_4.png", dpi=150, bbox_inches="tight")
plt.show()
