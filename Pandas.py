# read and write

# from operator import truediv
# from tkinter.tix import COLUMN
# import pandas as pd

# x = r"C:\Users\aksha\Desktop\BankNifty_NSE.xlsx"

# df = pd.read_csv(x, header=0, index_col=0) # df = dataframe

# print(df.head(5))

# indexing and selecting data

# print(df.head()) # .head return the first 5 rows
# print(df.tail()) # .tail return the last 5 rows

# print(df.size) # total number of data
# print(df.shape) # number of rows and columns
# print(df.ndim) # number of dimention

# .loc

# data = df.loc[['Afghanistan', 'Algeria'], ['WHO_REGION', 'VACCINES_USED'] ]
# print(data)

# df.loc['Algeria', 'VACCINES_USED'] = "Sputnik"

# data = df.loc['Algeria', 'VACCINES_USED']

# Pandas = Descriptive Statistics

# df.dropna(axis=0, inplace=True)

# print(df.head())

# print(df.iloc[:, 5].median())

# Pandas = Statistical Function

#  = r"C:\Users\aksha\Desktop\BankNifty_NSE.xlsx"

from fileinput import close
from tkinter import N
import pandas as pd

df = pd.read_csv(r'C:\Users\aksha\Desktop\BankNifty_NSE.csv', header= 0, index_col= 0)

df_percent_close = df.loc[:, 'Close']

df ['% Change'] = df_percent_close.pct_change()

df_percent_open = df.loc[:, 'Open']

df ['% Change Open'] = df_percent_open.pct_change()

x = (df.head(20))

y = (df_percent_open.cov(df_percent_close))

z = (df_percent_open.corr(df_percent_close))

print(x) 
print("")

print("Coverience = ", + y)
print("")

print("Correlation = ", + z)
print("")