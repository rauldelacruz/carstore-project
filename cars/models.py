from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

# Create your models here.

class Car(models.Model):
    year_choice = []
    for r in range(1900, (datetime.now().year+1)):
        year_choice.append((r,r))

    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('ABS', 'ABS'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Heated seats', 'Heated seats'),
        ('Central locking', 'Central locking'),
        ('Parking sensors', 'Parking sensors'),
        ('Power Steering', 'Power Steering'),
        ('Rear View Camera', 'Rear View Camera'),
        ('Electric windows', 'Electric windows'),
        ('Start/Stop', 'Start/Stop'),
        ('Traction control', 'Traction control'),
        ('ESP', 'ESP'),
        ('4-wheel drive', '4-wheel drive'),
        ('Alarm', 'Alarm'),
        ('Climate control', 'Climate control'),
    )

    door_choices = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    body_style_choices = (
        ('Hatchback', 'Hatchback'),
        ('Saloon', 'Saloon'),
        ('Estate', 'Estate'),
        ('Van', 'Van'),
        ('MPV', 'MPV'),
        ('SUV', 'SUV'),
        ('Convertible', 'Convertible'),
        ('Coupe', 'Coupe'),
        ('Truck', 'Truck'),
    )

    fuel_type_choices = (
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid'),
    )

    transmission_choices = (
        ('Automatic', 'Automatic'),
        ('Manual', 'Manual')
    )

    condition_choices = (
        ('Used', 'Used'),
        ('New', 'New'),
        ('Accidented', 'Accidented')
    )

    title = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    year = models.IntegerField(('year'), choices=year_choice)
    model = models.CharField(max_length=100)
    condition = models.CharField(choices = condition_choices, max_length=100)
    price = models.IntegerField()
    description = RichTextField()
    car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    features = MultiSelectField(choices=features_choices)
    body_style = models.CharField(choices= body_style_choices, max_length=100)
    engine = models.CharField(max_length=100, blank=True)
    transmission = models.CharField(choices= transmission_choices, max_length=100)
    mileage = models.IntegerField()
    doors = models.CharField(choices=door_choices, max_length=10)
    passengers = models.IntegerField()
    fuel_type = models.CharField(choices= fuel_type_choices, max_length=100)
    no_of_owners = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add = True)

    def __str__(self) -> str:
        return self.title
