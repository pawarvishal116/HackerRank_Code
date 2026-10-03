import pandas as pd

df = pd.read_csv("data_cleaning_sample.csv")
print(df)

print(df.isnull())              # True for NaNs
print(df.isnull().sum())        # Count missing per column

print(df.dropna())              # Drop rows with *any* missing values
print(df.dropna(axis=1))        # Drop columns with missing values

print(df.ffill())               # Forward fill
print(df.bfill())               # Backward fill
print(df.fillna(0))             # Replace NaN with 0

#df = df["Age"].fillna(df["Age"].mean())         # Replace with mean
#print(df)

print(df.duplicated())          # True for duplicates
print(df.drop_duplicates())     # Remove duplicate rows
print(df.duplicated(subset=["Name", "Age"]))

print(df["Name"].str.lower())                           # Converts all names to lowercase.
print(df["City"].str.contains("Delhi", case=False))     # Checks if 'delhi' is in the city name, case-insensitive.
print(df["Email"].str.split("@"))                       # Outputs a pandas Series where each element is a list of strings (the split parts). This is where a Python list comes into play, but the outer object is still a pandas Series.

'''Type Conversions with .astype()
Convert column data types:'''

#df["Age"] = df["Age"].astype(int)
#print(df)

#df["Join Date"] = pd.to_datetime(df["Join Date"])
#print(df)


## .apply() → Apply any function to rows or columns
df["Age_Group"] = df["Age"].apply(lambda x: "Adult" if x >= 25 else "Minor")
print(df)

## map() → Element-wise mapping for Series
gender_map = {"M": "Male", "F": "Female"}
df["Gender"] = df["Gender"].map(gender_map)
print(df)

## .replace() → Replace specific values
df["City"] = df["City"].replace({"Delhi": "New Delhi", "Mumbai": "Navi Mumbai"})
print(df)