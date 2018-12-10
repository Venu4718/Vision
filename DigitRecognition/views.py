from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import numpy as np
from urllib.request import urlretrieve
from PIL import Image
import PIL
from django.http import JsonResponse
from .utils import create_model
import matplotlib.pyplot as plt
# Create your views here.


def index(request):
    return render(request, 'Vision/base.html')

def digit(request):
    return render(request, 'DigitRecognition/digit.html')

@csrf_exempt
def detect(request):
    respon = request.POST['image64']
    filename, m = urlretrieve(respon)
    baseheight = 28
    img = Image.open(filename).convert('L')
    hpercent = (baseheight / float(img.size[1]))
    wsize = int((float(img.size[0]) * float(hpercent)))
    img = img.resize((wsize, baseheight), PIL.Image.ANTIALIAS)
    img = np.array(img.getdata()).reshape(1,28,28)
    model = create_model()
    plt.imshow(img.reshape(28,28))
    prediction = np.argmax(model.predict(img))
    return JsonResponse({'data':str(prediction)})