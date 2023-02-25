
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
from django.http import HttpResponseRedirect



def inquiry(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        user_id = request.POST['user_id']
        car_title = request.POST['car_title']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        city = request.POST['city']
        email = request.POST['email']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
        
        if request.user.is_authenticated:
            # userid = request.user.id
            has_contacted = Contact.objects.all().filter(user_id = user_id, car_id = car_id)
            
            if has_contacted:
                messages.error(request, 'Sorry, but you have already contacted regarding this automobile')
                return redirect('/cars/'+car_id)
        
        contact = Contact.objects.create(
            car_id = car_id, car_title = car_title,
            user_id = user_id, first_name = first_name,
            last_name = last_name, customer_need = customer_need,
            city = city, state = state, email = email, phone = phone,
            message = message,
        )
        
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        
        send_mail(
        'New car inquiry',
        'You have new car inquire for the car ' + car_title + '\nPlease login to your admin panel for more information!',
        'kaidu219@gmail.com',
        [admin_email],
        fail_silently=False,
        )
           
        contact.save()
        messages.success(request, 'Your request has been submited, we will get back to you shortly')
        return redirect('/cars/'+car_id)
        

def delete_inquiry(request, car_id):
    Contact.objects.filter(car_id = car_id)
    messages.success(request, 'Your inquiry was succes')