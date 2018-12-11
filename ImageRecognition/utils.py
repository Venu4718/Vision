import tensorflow as tf
from tensorflow.keras.initializers import glorot_uniform
def load_model():
    json_file = open('C:/Users/prasa/PycharmProjects/Vision/ImageRecognition/static/json/Image_model_v2.json', 'r')
    model = json_file.read()
    json_file.close()
    with tf.keras.utils.CustomObjectScope({'GlorotUniform': glorot_uniform()}):
        model = tf.keras.models.model_from_json(model)
    model.load_weights('C:/Users/prasa/PycharmProjects/Vision/ImageRecognition/static/h5/image_Inception_v3.h5')
    return model