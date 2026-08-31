
import pandas as pd
import numpy as np
 
arr = np.array([[1, 2], [3, 4]])
df = pd.DataFrame(arr, columns=["A", "B"])
print(df)

df = pd.read_csv("pandas-data.csv")
print(df)
print(df.head())
print(df.tail())
print(df.describe())