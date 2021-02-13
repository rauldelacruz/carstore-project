from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage,Paginator, PageNotAnInteger
from .models import Car

# Create your views here.
def cars(request):
    cars = Car.objects.order_by('-created_date')
    paginator = Paginator(cars, 6)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    makes = Car.objects.values_list('make', flat=True).distinct().order_by('make')
    locations = Car.objects.values_list('location', flat=True).distinct().order_by('location')
    years = Car.objects.values_list('year', flat=True).distinct().order_by('year')
    body_styles = Car.objects.values_list('body_style', flat=True).distinct()
    transmissions = Car.objects.values_list('transmission', flat=True).distinct()
    data = {
        'cars': paged_cars,
        'makes': makes,
        'locations': locations,
        'years': years,
        'body_styles': body_styles,
        'transmissions': transmissions,
    }
    return render(request, 'cars/cars.html', data)

def car_details(request, id):
    car = get_object_or_404(Car, pk=id)
    data = {
        'car': car,
    }
    return render(request, 'cars/car_details.html', data)

def search(request):
    cars = Car.objects.order_by('-created_date')
    makes = Car.objects.values_list('make', flat=True).distinct().order_by('make')
    locations = Car.objects.values_list('location', flat=True).distinct().order_by('location')
    years = Car.objects.values_list('year', flat=True).distinct().order_by('year')
    body_styles = Car.objects.values_list('body_style', flat=True).distinct()
    transmissions = Car.objects.values_list('transmission', flat=True).distinct()
    
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(title__icontains=keyword)

    if 'make' in request.GET:
        make = request.GET['make']
        if make:
            cars = cars.filter(make__iexact=make)

    if 'location' in request.GET:
        location = request.GET['location']
        if location:
            cars = cars.filter(location__iexact=location)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)

    data = {
        'cars': cars,
        'makes': makes,
        'locations': locations,
        'years': years,
        'body_styles': body_styles,
        'transmissions': transmissions,
    }
    return render(request, 'cars/search.html', data)
 