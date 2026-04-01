# Simple Deep Learning Model using TensorFlow

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np

# Sample dataset
x = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([2, 4, 6, 8, 10], dtype=float)

# Build model
model = keras.Sequential([
    layers.Dense(1, input_shape=[1])
])

# Compile model
model.compile(optimizer='sgd', loss='mean_squared_error')

# Train model
model.fit(x, y, epochs=100)

# Test prediction
print("Prediction for 6:", model.predict([6.0]))f