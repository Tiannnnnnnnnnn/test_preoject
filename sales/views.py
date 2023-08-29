from django.shortcuts import render

from django.http import HttpResponse
import os

def img_return(request):
    with open(os.getcwd() + "/sales/imgs/water.jpg", 'rb') as f:
        img_a = f.read()

    return HttpResponse(img_a, content_type = 'image/jpg')

# Create your views here.
