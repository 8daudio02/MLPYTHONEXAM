import pandas as pd
df = pd.read_csv("data.csv")
print(df)
print(df.head())
print(df.info())
print(df.describe())
print(df['totalprofit'].describe())
