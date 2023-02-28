from django.shortcuts import render, redirect
from .models import Team
from cars.models import Car 
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm



# Create your views here.
def index(request):
   teams = Team.objects.all()
   featured_cars = Car.objects.all().order_by('-created_date').filter(is_featured=True)
   model_search = Car.objects.order_by('model').values_list('model', flat=True).distinct
   city_search = Car.objects.order_by('city').values_list('city', flat=True).distinct
   year_search = Car.objects.order_by('-year').values_list('year', flat=True).distinct
   bs_search = Car.objects.order_by('body_style').values_list('body_style', flat=True).distinct

   all_cars = Car.objects.order_by('-created_date')
   context = {
      'teams': teams,
      'title': 'Home',
      'featured_cars': featured_cars,
      'all_cars': all_cars,
      'model_search': model_search,
      'city_search': city_search,
      'year_search': year_search,
      'bs_search': bs_search,
   }
   return render(request, 'website/index.html', context)


def contact(request):
   if request.method == 'POST':
      form = ContactForm(request.POST)

      if form.is_valid():

         full_name = form.cleaned_data['full_name']
         email = form.cleaned_data = ['email']
         subject = form.cleaned_data = ['subject']
         phone = form.cleaned_data = ['phone'] 
         message = form.cleaned_data = ['message']

         message_mail = f'Your have massage in CarSelling Platform from {full_name} regarding: {message} \n\n\Sender Details: Phone: {phone}; Email: {email}'

         admin_info = User.objects.get(is_superuser=True)
         admin_email = admin_info.email


         send_mail(
            subject,
            mark_safe(message_mail),
            email,
            ['carsellplatformdjango@gmail.com', admin_email],
            fail_silently=False,

         )
         messages.success(request, 'Your message has been successfully send!')
   else:
      form = ContactForm()
      # return redirect('contact', {'form': form})
   
   
   context = {
      'title': 'Contact Us',
      'form': form,
   }
   return render(request, 'website/contact.html', context)

def about(request):
   teams = Team.objects.all()
   context = {
      'teams': teams,
      'title': 'About Us'
   }
   return render(request, 'website/about.html', context)

def services(request):

   context = {
      'title': 'Services'
   }
   return render(request, 'website/services.html', context)