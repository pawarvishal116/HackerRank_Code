import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error

# 1. Load the data

housing = pd.read_csv("housing.csv")  # Load the housing dataset from a CSV file

# 2. Create stratified train-test split based on income category

housing["income_category"] = pd.cut(housing["median_income"],
                                    bins=[0, 1.5, 3.0, 4.5, 6.0, np.inf],  # Define bins for income categories
                                    labels=[1, 2, 3, 4, 5])  # Assign labels to the income categories

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)  # Create a stratified shuffle split object

for train_index, test_index in split.split(housing, housing["income_category"]):
    strat_train_set = housing.loc[train_index].drop("income_category", axis=1)  # Create the stratified training set
    strat_test_set = housing.loc[test_index].drop("income_category", axis=1)  # Create the stratified test set


# 3. Work on a copy of the training set to avoid modifying the original data
housing = strat_train_set.copy()  # Create a copy of the training set for further processing

# 4. Separate features and target variable
housing_features = housing.drop("median_house_value", axis=1)  # Features (all columns except the target variable)
housing_labels = housing["median_house_value"].copy()  # Target variable (median house value)

# 5. Separate numerical and categorical columns
numerical_features = housing_features.select_dtypes(include=[np.number]).columns.tolist()  # Get the list of numerical feature column names
categorical_features = housing_features.select_dtypes(include=[object]).columns.tolist()  # Get the list of categorical feature column names    

# 6. Create a preprocessing pipeline for numerical features
numerical_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy="median")),  # Impute missing values with the median
    ('scaler', StandardScaler())  # Scale numerical features to have mean=0 and variance=1
])

# 7. Create a preprocessing pipeline for categorical features
categorical_pipeline = Pipeline([
    ('onehot', OneHotEncoder(handle_unknown='ignore'))  # One-hot encode categorical features, ignoring unknown categories
])

# 8. Combine the numerical and categorical pipelines into a single column transformer
preprocessor = ColumnTransformer([
    ('num', numerical_pipeline, numerical_features),  # Apply the numerical pipeline to numerical features
    ('cat', categorical_pipeline, categorical_features)  # Apply the categorical pipeline to categorical features
])

#9. Fit and transform the training data using the combined preprocessor
housing_prepared = preprocessor.fit_transform(housing_features)  # Fit the preprocessor on the training features and transform them into a preprocessed format

#10. Print the final data shape and final preprocessed data
print("Preprocessed data shape:", housing_prepared.shape)  # Print the shape of the preprocessed data

#11. print final dataframe with column names
# Get the column names for the one-hot encoded categorical features
df = pd.DataFrame(housing_prepared, columns=numerical_features + list(preprocessor.named_transformers_['cat']['onehot'].get_feature_names_out(categorical_features)))  # Create a DataFrame with the preprocessed data and appropriate column names
print("Final DataFrame with column names:\n", df.head())  # Print the first 5 rows of the final DataFrame with column names


# 12 . Linear Regression Model
lin_reg = LinearRegression()  # Create a Linear Regression model
lin_reg.fit(housing_prepared, housing_labels)  # Fit the Linear Regression model on the preprocessed training data and labels

# 13. Decision Tree Regressor Model
tree_reg = DecisionTreeRegressor(random_state=42)  # Create a Decision Tree Regressor model
tree_reg.fit(housing_prepared, housing_labels)  # Fit the Decision Tree Regress

# 14 . Random Forest Regressor Model
forest_reg = RandomForestRegressor(random_state=42)  # Create a Random Forest Regressor model
forest_reg.fit(housing_prepared, housing_labels)  # Fit the Random Forest Regress

# 14 . Predict on the test set and evaluate the models
# Prepare the test set using the same preprocessor

lin_predict = lin_reg.predict(housing_prepared)  # Predict using the Linear Regression model on the preprocessed training data
tree_predict = tree_reg.predict(housing_prepared)  # Predict using the Decision Tree Regressor model on the preprocessed training data
forest_predict = forest_reg.predict(housing_prepared)  # Predict using the Random Forest Regressor model on the preprocessed training data

# 15 . Calculate RMSE for each model
lin_rmse = np.sqrt(root_mean_squared_error(housing_labels, lin_predict))  # Calculate RMSE for Linear Regression model
tree_rmse = np.sqrt(root_mean_squared_error(housing_labels, tree_predict))  # Calculate RMSE for Decision Tree Regressor model
forest_rmse = np.sqrt(root_mean_squared_error(housing_labels, forest_predict))  #Calculate RMSE for Random Forest Regressor model   

#16 . Cross validation for Decision Tree and Random Forest models
from sklearn.model_selection import cross_val_score
import pandas as pd

# Evaluate Decision Tree model using cross-validation
tree_scores = cross_val_score(tree_reg, housing_prepared, housing_labels, scoring="neg_mean_squared_error", cv=10)  # Perform 10-fold cross-validation for Decision Tree model
tree_rmse_scores = np.sqrt(-tree_scores)  # Convert negative MSE scores to RMSE scores
print("Decision Tree RMSE scores:", tree_rmse_scores)  # Print the RMSE scores for Decision Tree model

# Evaluate Random Forest model using cross-validation
forest_scores = cross_val_score(forest_reg, housing_prepared, housing_labels, scoring="neg_mean_squared_error", cv=10)  # Perform 10-fold cross-validation for Random Forest model
forest_rmse_scores = np.sqrt(-forest_scores)  # Convert negative MSE scores to RMSE scores
print("Random Forest RMSE scores:", forest_rmse_scores)  # Print the RMSE scores for Random Forest model


