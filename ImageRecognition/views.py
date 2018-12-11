from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import tensorflow as tf
import numpy as np
from .utils import load_model
# Create your views here.

def index(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        img = fs.open(filename)
        img = tf.keras.preprocessing.image.load_img(img,target_size=(224,224))
        img = tf.keras.preprocessing.image.img_to_array(img)
        img = np.expand_dims(img,axis=0)
        img = tf.keras.applications.inception_v3.preprocess_input(img)
        try:
            model = load_model()
            prediction = tf.keras.applications.inception_v3.decode_predictions(model.predict(img))[0][0][1]
        except Exception as e:
            prediction = "# Something went worng #\n"+e
        return render(request,'ImageRecognition/index.html',{'uploaded_file_url': uploaded_file_url,'prediction':prediction})
    return render(request,'ImageRecognition/index.html')
