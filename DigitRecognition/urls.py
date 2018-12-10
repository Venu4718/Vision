from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('digit/',views.digit,name='digit'),
    path('digit/detect/',views.detect,name='detect'),
]