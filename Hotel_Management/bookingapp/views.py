"""
Creating Views
"""
from django.shortcuts import render
from .models import SliderImage,Room

# Create your views here.

def slider_view(request):
    fetch_slider_images = SliderImage.objects.all()
    fetch_room = Room.objects.all()
    data= {
        'slider_images': fetch_slider_images,
        'room' : fetch_room
    }
    return render(request,'index.html', data)


