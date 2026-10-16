import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

print(sns.get_dataset_names())

tips = sns.load_dataset('tips')
print(tips.head())


sns.lineplot(x="total_bill", y="tip", data=tips)
plt.title('Line Plot Example')
plt.show()
sns.set_theme(style="darkgrid")  # Options: whitegrid, dark, white, ticks


import pandas as pd

df = pd.DataFrame({
    "age": [22, 25, 47, 52, 46, 56, 55, 60, 34, 43],
    "salary": [25000, 27000, 52000, 60000, 58000, 62000, 61000, 65000, 38000, 45000],
    "gender": ["M", "F", "M", "F", "F", "M", "M", "F", "F", "M"]
})

sns.scatterplot(x="age", y="salary", hue="gender", data=df)
plt.title('Salary vs Age Scatter Plot')
plt.show()

