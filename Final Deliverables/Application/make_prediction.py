from tensorflow.keras.utils import load_img
from tensorflow.keras.utils import img_to_array
from keras.models import load_model
from numpy import argmax


def argmax(a):
    return list(a).index(max(a))


def load_image(filename):
    test_img = load_img(filename, color_mode = "grayscale", target_size=(28, 28))
    img = img_to_array(test_img)
    img = img.reshape(1, 28, 28, 1)
    img = img.astype('float32')
    img = img / 255.0
    return img


def predict():
    img = load_image('./images/sample.png')
    model = load_model('model/model.h5')

    predict_value = model.predict(img)
    digit = argmax(predict_value)
    return digit
