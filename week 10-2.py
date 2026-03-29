import pandas as pd
df = pd.read_csv("data2.csv")
print(df.sort_values(by=df.columns[0]))
print(df.sort_values(by=df.columns[0], ascending=False))
print(df[0:5])
print(df[2:8])
