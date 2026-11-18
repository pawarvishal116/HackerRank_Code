# Import TensorFlow library to work with deep learning models and datasets.
import tensorflow as tf

# Import Matplotlib's pyplot to display images/plots in the notebook or console.
import matplotlib.pyplot as plt

# Load the MNIST dataset from TensorFlow's built-in datasets.
# x_train and x_test are 28x28 grayscale images, while y_train and y_test are the labels (digits 0-9).
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Print the training data shape: number of samples, image height, image width.
print("Training data shape:", x_train.shape)

# Print the shape of training labels: number of training samples.
print("Training labels shape:", y_train.shape)

# Print the test data shape: number of test samples, image height, image width.
print("Test data shape:", x_test.shape)

# Print the shape of test labels: number of test samples.
print("Test labels shape:", y_test.shape)

# Create a figure with width 10 and height 2 inches to show multiple images in one row.
plt.figure(figsize=(10, 2))

# Loop through the first 10 images in the training set.
for i in range(10):
    # Create a subplot for each image: 1 row, 10 columns, current image position.
    plt.subplot(1, 10, i + 1)

    # Display the image in grayscale using the pixel values from the dataset.
    plt.imshow(x_train[i], cmap="gray")

    # Hide the axes to make the image look clean.
    plt.axis("off")

    # Show the digit label as the title above the image.
    plt.title(str(y_train[i]))

# Adjust spacing so all subplots fit nicely without overlap.
plt.tight_layout()

# Display the final plot on the screen.
plt.show()
