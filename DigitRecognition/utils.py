import tensorflow as tf
import json
def create_model():
    json_file = open("C:/Users/prasa/PycharmProjects/Vision/DigitRecognition/static/DigitRecognition/json/model.json", 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = tf.keras.models.model_from_json(loaded_model_json)
    loaded_model.load_weights("C:/Users/prasa/PycharmProjects/Vision/DigitRecognition/static/DigitRecognition/h5/digit_v2.h5")
    return loaded_model

