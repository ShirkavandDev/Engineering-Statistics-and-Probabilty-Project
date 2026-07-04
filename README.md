# Descriptive Analysis of Income-Decile Classification and Financial Behaviors among Iranians (2019–2023)

> **Engineering Statistics and Probability Project**<br>
> **Researcher:** Amirreza Shirkavand<br>
> **Course Instructor:** [Prof. Saeed Ghazanfari-Rad](https://scholar.google.com/citations?user=x1ms3cgAAAAJ)<br>
> Software: Python 3.13.1 · pandas · matplotlib · scipy<br>
> Dataset: Iranian Welfare Database, Ministry of Cooperatives, Labour and Social Welfare

---

## 📋 Project Overview

This project applies descriptive statistical methods to a large-scale administrative dataset (~1.7 million individuals, 48 variables) compiled by Iran's social welfare system for the purpose of income-decile classification and targeted-subsidy allocation (means-testing).

The questions addressed are:

1. How do average monthly bank card transaction volumes differ across the ten income-deciles?
2. Is there an upward trend in average monthly bank card transactions over the years 1398–1402?
3. Which variables are most strongly associated with a person's income-decile?

---

### 📦 Dataset

| File | Description |
|---|---|
| `nemone_2_darsadi_1402.part1.rar` | First part of the compressed dataset archive |
| `nemone_2_darsadi_1402.part2.rar` | Second part of the compressed dataset archive |
| `nemone_2_darsadi_1402.csv` | Extracted dataset file (1,697,816 rows × 48 columns) |

The dataset is a 2% sample from the Iranian Welfare Database, published by the Ministry of Cooperatives, Labour and Social Welfare after removal of confidential information.

**Dataset link:** https://refahdb.mcls.gov.ir/fa/downloaddata-دانلودداده

---

## 📊 Figures Summary

| Figure | Script | Description |
|--------|--------|-------------|
| Figure 1 | `Figure_1.py` | Histogram of age distribution |
| Figure 2 | `Figure_2.py` | Gender distribution |
| Figure 3 | `Figure_3.py` | Top 10 most populous provinces in the dataset |
| Figure 4 | `Figure_4.py` | Mean monthly card transactions by age group, split by gender |
| Figure 5 | `Figure_5.py` | Population count per income decile |
| Figure 6 | `Figure_6.py` | Boxplot of monthly card transactions (1402) by decile (top 3% outliers removed) |
| Figure 7 | `Figure_7.py` | Side-by-side boxplots: nominal vs inflation-adjusted card transactions (1398–1402) |
| Figure 8 | `Figure_8.py` | Spearman correlation bar chart: demographic/socioeconomic indicators vs income decile |
| Figure 9 | `Figure_9.py` | Car ownership rate and government employment rate by decile |
| Figure 10 | `Figure_10.py` | Urban residence share by income-decile |

---

## 🔎 Key Findings

- **A strong monotonic relationship exists between income-decile and monthly card transaction volume**, rising from ~14M Rial (decile 1) to ~416M Rial (decile 10) — a nearly 30× difference — confirming the decile classification aligns well with observed financial behavior.
- **Nominal transaction volumes grew substantially from 1398 to 1402; however, after adjusting for inflation using official inflation rates, real values remained relatively constant** (a slight upward trend from 1398–1401 was followed by a decline in 1402). The nominal growth was largely driven by Iran's high inflation rate.
- **The five variables most positively correlated with income decile are:** (1) Urban residence (ρ = +0.210), (2) Stock portfolio value (ρ = +0.208), (3) Insurance payer status (ρ = +0.166), (4) Business license ownership (ρ = +0.115), (5) Government employment (ρ = +0.097).
- **The five variables most negatively correlated with income decile are:** (1) Disability (ρ = −0.096), (2) Female gender (ρ = −0.053), (3) Malnutrition support (ρ = −0.023), (4) Retired-dependent status (ρ = −0.012), (5) Chronic illness (ρ = −0.011).
- **All correlations have absolute values below 0.3**, indicating that none of these variables alone is a strong predictor of income decile — the decile classification relies on a combination of many factors.
- Males consistently show higher card transaction volumes than females across all age groups, likely reflecting higher rates of formal employment and household financial management. Spending peaks around age 50 for males and age 40 for females, then declines in both groups.

---

## 🛠️ Installation & Usage

### 1. Clone the repository
```bash
git clone https://github.com/ShirkavandDev/Engineering-Statistics-and-Probabilty-Project.git

cd Engineering-Statistics-and-Probabilty-Project
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Extract the dataset
Extract the dataset files, then place nemone_2_darsadi_1402.csv in `figures/`.
### 3. Run a figure script
Each figure has its own standalone script. To run any of them from the project's root directory:
```bash
python figures/Figure_1.py
```
Output images are saved to `images/` (created automatically if not present).

### 4. Or run the full notebook
Open `figures/all_figures.ipynb` in Jupyter and run all cells.

---

## 📄 Report

The full written report (in Persian) is available as [`report.pdf`](./report.pdf). It follows the following structure:

1. Abstract
2. Introduction
3. Dataset Description
4. Data Analysis Using Descriptive Statistics
5. Discussion & Results
6. Conclusion
7. AI Tool Usage Statement
8. References
9. Glossary

---

## 📚 References

1. Iranian Welfare Database, Ministry of Cooperatives, Labour and Social Welfare. (2023). 2% Sample of the Iranian Welfare Database. https://refahdb.mcls.gov.ir/fa/downloaddata-دانلودداده
2. Daghigheh Data Analysis School. (2024, 16 June). Introduction to the Iranian Welfare Database. https://d-learn.ir/wellfare-data-bank
3. Mohammadi, H. (2026, 21 May). Subsidy eligibility conditional on passing the means test. IBENA. https://ibena.ir/fa/news/183279
4. Ghazanfari-Rad, S. (2025). Engineering Statistics and Probability Sample Project (`sample_project_01.pdf`). GitHub. https://github.com/saeedgrad/Engineering_Statistics
5. Central Bank of Iran. Inflation Rates. https://cbi.ir/Inflation/Inflation_fa.aspx