import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import StratifiedShuffleSplit

# Load the dataset
data = pd.read_csv("housing.csv")


'''
This code creates a new column income_category that categorizes the median_income into five bins. 
Each bin represents a range of income levels, allowing us to stratify our sampling based on these categories.
'''

# pd.cut(values, bins, labels) . It takes numerical values and puts them into different ranges.

data["income_category"] = pd.cut(data["median_income"],
                             bins=[0, 1.5, 3.0, 4.5, 6.0, np.inf],   # np.inf means positive infinity
                             labels=[1, 2, 3, 4, 5])




# Assume income_category is a column in the dataset created from median_income
# n_splits=1  -  Perform the train/test split one time.
#test_size=0.2  -  20% of the data will be used for testing, and 80% for training.
#random_state=42  -  Ensures reproducibility of the split.

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)

# Explain the split.split(data, data["income_category"]) method:
#"Split data, but maintain the distribution of income_category."

# Abolve split will return two sets of indices: one for the training set and one for the test set.Becaue
# of that we have used two variables train_index and test_index to store the indices of the training and test sets respectively.

for train_index, test_index in split.split(data, data["income_category"]):
    strat_train_set = data.loc[train_index]
    strat_test_set = data.loc[test_index]


#Explain the value_counts() method:
# This method counts the number of instances in each category of the income_category column.
#Explain the sort_index() method:
# This method sorts the index of the Series in ascending order.

for a in (strat_train_set, strat_test_set):
    a.drop(["income_category"], axis=1, inplace=True)  # Drop the income_category column from both training and test sets

df = strat_train_set.copy()  # Create a copy of the stratified training set to avoid modifying the original data
print(df.head())

df.to_excel("stratified_train_set.xlsx", index=False)  # Save the stratified training set to an Excel file without the index

data["income_category"].value_counts().sort_index().plot.bar(rot=0, grid=True)  
plt.title("Income Categories Distribution") 
plt.xlabel("Income Category")
plt.ylabel("Number of Instances")
plt.show()

 
