import pandas as pd

s = pd.Series([10, 20, 30])
print(s)

p = pd.Series([1, 2, 34], index=["a", "b", "z"])
print(p)


data = {
    "name": ["Vishal", "Pallavi", "Divisha"],
    "age": [32, 32, 2],
    "dob": [15, 19, 3]
}

df = pd.DataFrame(data)
print(df)
print(df.index)
print(df.columns)