
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

from cars.models import Car



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

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        car_owner = Car.objects.get(id = car_id)

        
        
        sent_email = ''

        if car_owner.owner:
            if car_owner.owner.email:
                car_email = car_owner.owner.email
            else:
                car_email = admin_email
            sent_email = car_email
        else:
            sent_email = admin_email

        if request.user.is_authenticated:
            # userid = request.user.id
            has_contacted = Contact.objects.all().filter(user_id = user_id, car_id = car_id)
            
            if has_contacted:
                messages.error(request, 'Sorry, but you have already contacted regarding this automobile')
                return redirect('cardetails', car_id)
        
        contact = Contact.objects.create(
            car_id = car_id, car_title = car_title,
            
            user_id = user_id, first_name = first_name,
            last_name = last_name, customer_need = customer_need,
            city = city, state = state, email = email, phone = phone,
            message = message,
        )


        send_mail(
            'New car inquiry',
            'You have new car inquire for the car ' + car_title + '\nPlease login to your admin panel for more information!',
            'carsellplatformdjango@gmail.com',
            [sent_email],
            fail_silently=False,
            )
        

           
        contact.save()
        messages.success(request, 'Your request has been submited, we will get back to you shortly')
        return redirect('/cars/cardetails/'+car_id)
        

def delete_inquiry(request, id):
    Contact.objects.filter(car_id = id).delete()
    messages.success(request, 'Your inquiry was successfully delete!')
    return redirect('/accounts/dashboard')