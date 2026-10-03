import pandas as pd

df = pd.read_csv("pandas-data.csv")
print(df)

# print column Actor and year . And 5 rows 
df = pd.read_csv("pandas-data.csv", usecols=["Actor", "Year"], nrows=5)
print(df)

df.to_csv("output.csv", index=False)

df = pd.read_excel("data.xlsx")
pd.read_excel("data.xlsx", sheet_name="Sales")
df.to_excel("output.xlsx", index=False)

with pd.ExcelWriter("report.xlsx") as writer:
    df1.to_excel(writer, sheet_name="Summary", index=False)
    df2.to_excel(writer, sheet_name="Details", index=False)


df = pd.read_json("data.json")