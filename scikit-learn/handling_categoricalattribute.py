import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit
import numpy as np
from sklearn.impute import SimpleImputer

data = pd.read_excel("stratified_train_set.xlsx")  # Load the stratified training set from the Excel file

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)

data["income_category"] = pd.cut(data["median_income"],
                             bins=[0, 1.5, 3.0, 4.5, 6.0, np.inf],   # np.inf means positive infinity
                             labels=[1, 2, 3, 4, 5])

for train_index, test_index in split.split(data, data["income_category"]):
    strat_train_set = data.loc[train_index]
    strat_test_set = data.loc[test_index]

housing = strat_train_set.drop("median_house_value", axis=1)  # Features
housing_labels = strat_train_set["median_house_value"].copy()  # Target variable

imputer = SimpleImputer(strategy="median")  # Create an imputer object with a median filling strategy
housing_num = housing.select_dtypes(include=[np.number])  # Select only numerical columns from the features as we have ocean_proximity as a string attribute and we cannot compute the median of categorical attributes. 
imputer.fit(housing_num)  # Fit the imputer on the training data

X = imputer.transform(housing_num)  # Transform the training data by replacing missing values with the median

housing = pd.DataFrame(X, columns=housing_num.columns, index=housing.index)  # Convert the transformed array back to a DataFrame with the original column names and index


housing['ocean_proximity'] = strat_train_set['ocean_proximity'].values  # Add the categorical column back to the DataFrame
print(housing.head())  # Display the first few rows of the transformed features with the categorical column added back

from sklearn.preprocessing import OneHotEncoder
cat_encoder = OneHotEncoder()

housing_cat = cat_encoder.fit_transform(housing[['ocean_proximity']])  # Fit and transform the categorical column using one-hot encoding

housing_cat_df = pd.DataFrame(housing_cat.toarray(), columns=cat_encoder.get_feature_names_out(['ocean_proximity']), index=housing.index)  # Convert the one-hot encoded array back to a DataFrame with appropriate column names and index
print(housing_cat_df)  # Display the one-hot encoded categorical data

df = pd.concat([housing, housing_cat_df], axis=1)  # Concatenate the original features with the one-hot encoded categorical data
print(df.head())  # Display the first few rows of the combined DataFrame