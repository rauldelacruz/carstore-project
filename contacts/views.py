from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

# Create your views here.

def inquiry(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        title = request.POST['title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        inquiry = request.POST['inquiry']
        location = request.POST['location']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already sent an inquiry for this car. Please wait until we get back to you.')
                return redirect('/cars/'+car_id)

        contact = Contact(car_id=car_id, title=title, user_id = user_id,
        first_name=first_name, last_name=last_name, inquiry=inquiry, location=location,
        email=email, phone=phone, message=message)

        contact.save()
        messages.success(request, 'Your inquiry has been submitted, we will get back to you shortly.')
        return redirect('/cars/'+car_id)