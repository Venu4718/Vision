import tensorflow.keras as tf
from tensorflow.keras.initializers import glorot_uniform
import numpy as np
import json
def load_model():
    json_file = open('C:/Users/prasa/PycharmProjects/Vision/ImageRecognition/static/ImageRecognition/json/Image_model_v2.json', 'r')
    model = json_file.read()
    json_file.close()
    with tf.utils.CustomObjectScope({'GlorotUniform': glorot_uniform()}):
        model = tf.models.model_from_json(model)
    model.load_weights('C:/Users/prasa/PycharmProjects/Vision/ImageRecognition/static/ImageRecognition/h5/image_Inception_v3.h5')
    return model