"""
Creating Views
"""
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import SliderImage,Room
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm , LoginForm

# Create your views here.

def slider_view(request):
    fetch_slider_images = SliderImage.objects.all()
    fetch_room = Room.objects.all()
    data= {
        'slider_images': fetch_slider_images,
        'room' : fetch_room
    }
    return render(request,'index.html', data)

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request,'signup.html', {'form': form})


def _login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            # Authenticate using your custom authentication backend
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('slider')
            return redirect('slider')
    else:
        # form = LoginForm()
        return render(request, 'login.html')
    return render(request, 'login.html')