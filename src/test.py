from tensorflow import keras
import numpy as np

model = keras.models.load_model('../mdl/test.keras')

print(model.predict(np.array([10.0])))