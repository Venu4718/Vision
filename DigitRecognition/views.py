from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'Vision/base.html')

def digit(request):
    return render(request, 'DigitRecognition/digit.html')