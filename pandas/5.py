import pandas as pd
df = pd.read_csv("pandas-data.csv")

print(df.sort_values("Year"))

print(df.sort_values(["Year", "IMDb"]))
print(df.sort_values("Year", ascending=False))
df2 = df.sort_values("Year", ascending=False).copy()
df3 = df.sort_values("Year", ascending=False).copy()

print(df2.reset_index(drop=True))

print(df3.sort_index())

print(df3["IMDb"].rank(method="dense"))

print(df3.rename(columns={"Actor": "Hero"}))            # Change column name
print(df2.rename(index={0: "HI", 1: "Bi"}))             # Change row index name

