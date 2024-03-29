from tensorflow import keras
import numpy as np


# model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
# model.compile(optimizer='sgd', loss='mean_squared_error')

def create_model():
    model = karas.Sequential([keras.layers.Dense(units=1, input_shape=[1])])


fs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
season = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float) 

model.fit(fs, season, epochs=100)

model.save('../mdl/test.keras')

# print(model.predict(np.array([10.0])))