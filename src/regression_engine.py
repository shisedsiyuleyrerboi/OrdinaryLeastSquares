import statsmodels.api as stats
import pandas as pd
import tkinter as tk
from tkinter import filedialog

 
root = tk.Tk()
root.withdraw()
path = filedialog.askopenfilename(title = "Select your dataset", filetypes = [('Excel',"*.xlsx *.xls")])

df = pd.read_excel(path)

ratios = ['GrossMargin', 'OperatingMargin', 'CurrentRatio', 'DebtToEquity', 'ROA']
for col in ratios + ['ROE']:
    df[col] = df[col].astype(str).str.replace('%','').str.replace(',','').str.replace('—','')
    df[col] = pd.to_numeric(df[col], errors='coerce')

df = df.dropna()

y = df['ROE']
x = df[ratios]

x = stats.add_constant(x)
model = stats.OLS(y, x).fit()