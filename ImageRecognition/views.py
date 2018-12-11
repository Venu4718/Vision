from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import scipy.misc
import numpy as np
# Create your views here.

def index(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        h = 100
        w = 100
        img = fs.open(filename)
        img = scipy.misc.imread(img,flatten=False,mode='RGB')
        img = np.resize(img,(h,w,3))
        print(img.shape)
        return render(request,'ImageRecognition/index.html',{'uploaded_file_url': uploaded_file_url})
    return render(request,'ImageRecognition/index.html')