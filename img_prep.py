from keras.preprocessing import image
import numpy as np
import keras


def prepare_image(img_array):
    img_array_expanded_dims = np.expand_dims(img_array, axis = 0)
    return keras.applications.mobilenet.preprocess_input(img_array_expanded_dims)