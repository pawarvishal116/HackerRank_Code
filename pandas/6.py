import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Math': [85, 78, 92],
    'Science': [90, 82, 89],
    'English': [88, 85, 94]
}
 
df = pd.DataFrame(data)
 
# Display the DataFrame
print(df)

af = df.melt(id_vars=["Name"], value_vars=["Math", "Science", "English"], var_name="Subject", value_name="Score")
print(af)

print(af.pivot(index="Name", columns="Subject", values="Score"))
print(af.pivot_table(index="Name", columns="Subject", values="Score", aggfunc="mean"))
