import tensorflow as tf  # Import TensorFlow, the deep learning library used to build and train the neural network.
from tensorflow.keras.models import Sequential  # Import Sequential so we can create a model layer by layer in order.
from tensorflow.keras.layers import Dense, Flatten  # Import Dense (fully connected layer) and Flatten (reshape image into 1D vector).
from tensorflow.keras.datasets import mnist  # Import the MNIST dataset, which contains handwritten digits from 0 to 9.
from tensorflow.keras.utils import to_categorical  # Import function that converts labels like 3 into one-hot encoding like [0,0,0,1,0,0,0,0,0,0].

# Load the dataset into training and testing sets.
# x_train and x_test are image arrays, while y_train and y_test are their class labels.
# Example: x_train[i] is an image of a digit and y_train[i] is the correct digit it represents.
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize the pixel values from 0-255 to 0-1.
# This is important because neural networks train better when inputs are small and scaled.
# Example: pixel value 255 becomes 1.0, value 0 stays 0.0.
x_train = x_train / 255.0
x_test = x_test / 255.0

# Convert the label values (0 through 9) into one-hot encoded vectors.
# This helps the model compare its output probabilities against the true class.
# Example: label 7 becomes [0,0,0,0,0,0,0,1,0,0].
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# Create a sequential neural network model.
# Sequential means layers are added one after another in a linear order.
model = Sequential([
    Flatten(input_shape=(28, 28)),     # Flatten the 28x28 image into a 784-element vector because a dense layer expects 1D input.
    Dense(128, activation='relu'),     # Add a hidden layer with 128 neurons. ReLU removes negative values and keeps positive values.
    Dense(10, activation='softmax')    # Add output layer with 10 neurons, one for each digit. Softmax converts them into class probabilities.
])

# Compile the model by specifying how training should occur.
# optimizer='adam' uses the Adam optimization algorithm to update weights efficiently.
# loss='categorical_crossentropy' measures the difference between predicted and true class probabilities.
# metrics=['accuracy'] tracks how often the model predicts the correct class.
model.compile(
    optimizer='adam',                 # Adam is a popular optimizer for deep learning models.
    loss='categorical_crossentropy',  # Good choice for multi-class classification where the output is a probability distribution.
    metrics=['accuracy']              # Measures the percentage of correct predictions.
)

# Train the model using the training data.
# epochs=5 means the network will pass through the training data 5 times.
# batch_size=32 means it updates weights after every 32 samples.
model.fit(x_train, y_train, epochs=5, batch_size=32)

# Evaluate the trained model on the test set to measure performance on unseen data.
# The function returns test loss and accuracy.
test_loss, test_acc = model.evaluate(x_test, y_test)

# Print the model's test accuracy with 4 digits after the decimal point.
# Example output: Test accuracy: 0.9765
print(f"Test accuracy: {test_acc:.4f}")