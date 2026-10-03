import pandas as pd
df = pd.read_csv("pandas-data.csv")
print(df)
print(df["Actor"])                       # printing column
print(df["Actor"][2])
print(df[["Actor", "Year"]])
print(df.loc[1])                         # printing rows by index 
print(df.iloc[1])                        # printing rows by position
print(df.loc[1, "Actor"])                # values at index 1 and column Actor
print(df.iloc[1, 0])                     # values at position 1 and column 0
print(df.at[1, "Actor"])
print(df.iat[1,1])
print(df[df["Year"]>= 2018])
print(df[(df["Year"] > 2018) & (df["IMDb"] > 6)] )

print(df.query("Year > 2018 and IMDb > 6"))

col = "Film"
print(df.query(f"{col} == 'War'"))

Im = 7.0
print(df.query("IMDb > @Im"))