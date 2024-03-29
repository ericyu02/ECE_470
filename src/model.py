from tensorflow import keras
import numpy as np

model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')

xs = np.array([4.28658537, 4.73417722, 4.2195122,  4.43636364], dtype=float)
ys = np.array([0.01, 0.02, 0.03, 0.04], dtype=float) 

model.fit(ys, xs, epochs=200)

model.save('../mdl/test.keras')

print(model.predict(np.array([0.05])))