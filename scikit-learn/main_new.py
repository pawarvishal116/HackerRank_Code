import os  # Import the OS module to work with file paths and check whether model files already exist.
import pandas as pd  # Import pandas to load, clean, and manipulate tabular data.
import numpy as np  # Import NumPy for numeric operations and income-category bin creation.
import joblib  # Import joblib to save and load the trained model and preprocessing pipeline.

from sklearn.model_selection import StratifiedShuffleSplit  # Import train/test split strategy that keeps class distribution balanced.
from sklearn.pipeline import Pipeline  # Import Pipeline to chain preprocessing steps in order.
from sklearn.compose import ColumnTransformer  # Import ColumnTransformer to apply different transformations to numeric and categorical columns.
from sklearn.impute import SimpleImputer  # Import SimpleImputer to fill missing numeric values with a chosen statistic.
from sklearn.preprocessing import StandardScaler, OneHotEncoder  # Import scalers and encoder for feature preprocessing.
from sklearn.ensemble import RandomForestRegressor  # Import the regression model used for prediction.

MODEL_FILE = "model.pkl"  # Name of the saved trained model file.
PIPELINE_FILE = "pipeline.pkl"  # Name of the saved preprocessing pipeline file.

def build_pipeline(num_attribs, cat_attribs):  # Define a function that creates the full preprocessing pipeline for both numeric and categorical data.
    num_pipeline = Pipeline([  # Create a pipeline for numerical features.
        ("imputer", SimpleImputer(strategy="median")),  # Replace missing numeric values with the median of each column.
        ("scaler", StandardScaler())  # Standardize numeric features to zero mean and unit variance.
    ])
    cat_pipeline = Pipeline([  # Create a pipeline for categorical features.
        ("onehot", OneHotEncoder(handle_unknown="ignore"))  # Convert categories into one-hot encoded vectors while ignoring unknown categories during inference.
    ])
    full_pipeline = ColumnTransformer([  # Combine the numeric and categorical pipelines into one transformer.
        ("num", num_pipeline, num_attribs),  # Apply the numeric pipeline to the numeric attribute list.
        ("cat", cat_pipeline, cat_attribs)  # Apply the categorical pipeline to the categorical attribute list.
    ])
    return full_pipeline  # Return the configured preprocessing pipeline for later fitting and transforming.

if not os.path.exists(MODEL_FILE):  # If the trained model file does not already exist, train a new model.
    # TRAINING PHASE  # Mark the block as the model-training section.
    housing = pd.read_csv("housing.csv")  # Load the dataset containing housing information.
    housing['income_cat'] = pd.cut(housing["median_income"],  # Create a new income category column based on median income ranges.
                                   bins=[0.0, 1.5, 3.0, 4.5, 6.0, np.inf],  # Define the income thresholds for each category.
                                   labels=[1, 2, 3, 4, 5])  # Label each income range with an integer category.
    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)  # Create a train/test split that preserves the class distribution of income categories.
    for train_index, _ in split.split(housing, housing['income_cat']):  # Loop through the generated split to select the training rows.
        housing = housing.loc[train_index].drop("income_cat", axis=1)  # Keep only the training data and drop the temporary income category used for splitting.

    housing_labels = housing["median_house_value"].copy()  # Store the target variable (house value) separately from the features.
    housing_features = housing.drop("median_house_value", axis=1)  # Remove the target column to keep only the predictive features.

    num_attribs = housing_features.drop("ocean_proximity", axis=1).columns.tolist()  # Collect all numeric feature names except the categorical ocean proximity column.
    cat_attribs = ["ocean_proximity"]  # Define the categorical feature list for the preprocessing pipeline.

    pipeline = build_pipeline(num_attribs, cat_attribs)  # Build the preprocessing pipeline based on the selected feature lists.
    housing_prepared = pipeline.fit_transform(housing_features)  # Fit the pipeline on the training features and transform them into model-ready numerical data.

    model = RandomForestRegressor(random_state=42)  # Initialize the random forest regressor with a fixed random state for reproducibility.
    model.fit(housing_prepared, housing_labels)  # Train the regressor using the transformed training features and target labels.

    # Save model and pipeline  # Mark the save section.
    joblib.dump(model, MODEL_FILE)  # Save the trained model to disk for future use.
    joblib.dump(pipeline, PIPELINE_FILE)  # Save the preprocessing pipeline so new input is transformed the same way.

    print("Model trained and saved.")  # Display a confirmation message after training and saving.

else:  # If a trained model already exists, use it for prediction instead of retraining.
    # INFERENCE PHASE  # Mark the block as the prediction/inference phase.
    model = joblib.load(MODEL_FILE)  # Load the saved trained model from disk.
    pipeline = joblib.load(PIPELINE_FILE)  # Load the saved preprocessing pipeline from disk.

    input_data = pd.read_csv("input.csv")  # Load the new input dataset to predict on.
    transformed_input = pipeline.transform(input_data)  # Transform the raw input with the same preprocessing steps used during training.
    predictions = model.predict(transformed_input)  # Use the model to generate predictions for the transformed input.
    input_data["median_house_value"] = predictions  # Add predicted house values as a new column to the input dataset.

    input_data.to_csv("output.csv", index=False)  # Save the predictions to an output CSV file without the row index.
    print("Inference complete. Results saved to output.csv")  # Print a success message indicating the prediction output file was created.