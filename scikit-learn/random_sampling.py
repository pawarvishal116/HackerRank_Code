import numpy as np
import pandas as pd

def shuffle_and_split_data(data, test_ratio):
    np.random.seed(42)                  # Whenever run this code, generate the same random sequence.
    shuffled_indices = np.random.permutation(len(data))   # Give me all the row numbers, but in random order.
    test_set_size = int(len(data) * test_ratio)    # e.g 10 * 0.2 = 2     
    test_indices = shuffled_indices[:test_set_size]      # Take the first 2 element as test set size is 
    train_indices = shuffled_indices[test_set_size:]     # Start from index 2 and take everything after that.
    return data.iloc[train_indices], data.iloc[test_indices]     # its returing two  dataset

data = pd.read_csv("housing.csv")
train_data , test_data = shuffle_and_split_data(data, 0.2)  # 20% testing data

print("Training data:")
print(train_data)

print("\nTesting data:")
print(test_data)

