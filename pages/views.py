from cars.models import Car
from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    team = TeamMember.objects.all()
    featured_cars = Car.objects.order_by('created_date').filter(is_featured=True)[:8]
    latest_cars = Car.objects.order_by('created_date')[:6]
    makes = Car.objects.values_list('make', flat=True).distinct().order_by('make')
    locations = Car.objects.values_list('location', flat=True).distinct().order_by('location')
    years = Car.objects.values_list('year', flat=True).distinct().order_by('year')
    body_styles = Car.objects.values_list('body_style', flat=True).distinct()
    transmissions = Car.objects.values_list('transmission', flat=True).distinct()

    data = {
        'team': team,
        'featured': featured_cars,
        'latest': latest_cars,
        'makes': makes,
        'locations': locations,
        'years': years,
        'body_styles': body_styles,
        'transmissions': transmissions,
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
