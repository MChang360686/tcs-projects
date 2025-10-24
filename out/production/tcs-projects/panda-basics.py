import pandas as pd

df = pd.read_csv("info.csv")

for i in range(0, len(df)):
    if df.loc[i, 'price'] < 60:
        df.loc[i, 'purchased'] = True
    else:
        continue

df.to_csv("info.csv", index=False)