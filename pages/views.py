from cars.models import Car
from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    team = TeamMember.objects.all()
    featured_cars = Car.objects.order_by('created_date').filter(is_featured=True)[:8]
    latest_cars = Car.objects.order_by('created_date')[:6]
    data = {
        'team': team,
        'featured': featured_cars,
        'latest': latest_cars
    }
    return render(request, 'pages/home.html', data)

def about(request):
    team = TeamMember.objects.all()
    data = {
        'team': team,
    }
    return render(request, 'pages/about.html', data)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')
