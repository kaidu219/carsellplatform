from django.shortcuts import render
from .models import Team
from cars.models import Car 


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
   context = {
      'title': 'Contact Us'
   }
   return render(request, 'website/contact.html', context)

def about(request):

   context = {
      'title': 'About Us'
   }
   return render(request, 'website/about.html', context)

def services(request):

   context = {
      'title': 'Services'
   }
   return render(request, 'website/services.html', context)