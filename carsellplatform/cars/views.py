from django.shortcuts import render, redirect, get_object_or_404
from .models import CarPhoto, Car
from django.core.paginator import Paginator
from .forms import CarForm, CarPhotoForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .utils import get_search_filters

# Create your views here.
def allcars(request):
    allcars = Car.objects.all()
    paginator = Paginator(allcars, 2)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    # model_search = Car.objects.order_by('model').values_list('model', flat=True).distinct
    # city_search = Car.objects.order_by('city').values_list('city', flat=True).distinct   
    # year_search = Car.objects.order_by('-year').values_list('year', flat=True).distinct   
    # bs_search = Car.objects.order_by('body_style').values_list('body_style', flat=True).distinct
    # transmission_search = Car.objects.order_by('transmission').values_list('transmission', flat=True).distinct


    context = {
        'paged_cars': paged_cars,
        'allcars': allcars,
        'title': 'Cars',
        **get_search_filters(),
        # 'model_search': model_search,
        # 'city_search': city_search,
        # 'year_search': year_search,
        # 'bs_search': bs_search,
        # 'transmission_search': transmission_search,
    }

    return render(request, 'cars/cars.html', context=context)


def cardetails(request, id):
    car = Car.objects.get(pk = id)
    cars = Car.objects.get(pk = id).car_title
    context = {
        'car': car,
        'title': cars
    }
    return render(request, 'cars/car-details.html', context=context)  



def search(request):
    cars = Car.objects.order_by('-created_date')
    # model_search = Car.objects.order_by('model').values_list('model', flat=True).distinct
    # city_search = Car.objects.order_by('city').values_list('city', flat=True).distinct   
    # year_search = Car.objects.order_by('-year').values_list('year', flat=True).distinct   
    # bs_search = Car.objects.order_by('body_style').values_list('body_style', flat=True).distinct
    # transmission_search = Car.objects.order_by('transmission').values_list('transmission', flat=True).distinct
    # price_search = Car.objects.order_by('price').values_list('price', flat=True)

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains = keyword)

    if 'model' in request.GET:
        model = request.GET['model']
        
        if model:
            cars = cars.filter(model__iexact = model)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        
        if body_style:
            cars = cars.filter(body_style__iexact = body_style)

    if 'city' in request.GET:
        city = request.GET['city']
        
        if city:
            cars = cars.filter(city__iexact = city)

    if 'year' in request.GET:
        year = request.GET['year']
        
        if year:
            cars = cars.filter(year__iexact = year)

    if 'transmission' in request.GET:
        transmission = request.GET['transmission']
        
        if transmission:
            transmission = cars.filter(transmission__iexact = transmission)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']

        if max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)

    context = {
        'cars': cars,
        # 'model_search': model_search,
        # 'city_search': city_search,
        # 'year_search': year_search,
        # 'bs_search': bs_search,
        # 'transmission_search': transmission_search,
        # 'price_search':price_search,
        **get_search_filters(),
        
    }
    return render(request, 'cars/search.html', context)

@login_required(login_url='login')
def add_car(request):
    if request.method == 'POST':
        car_form = CarForm(request.POST, request.FILES)
        cars_photo_form = CarPhotoForm(request.POST, request.FILES)

        if car_form.is_valid() and cars_photo_form.is_valid():
            car = car_form.save(commit=False)
            car.owner = request.user
            car.save()
            cars_photo_form.instance.car_photo = car
            cars_photo_form.save()

            #Saving main photo
            if 'car_main_photo' in request.FILES:
                car.car_main_photo = request.FILES['car_main_photo']
                car.save()

            return redirect('cardetails', id = car.id) 
        
    else:
        car_form = CarForm()
        cars_photo_form = CarPhotoForm()    

    context = {
        'car_form': car_form,
        'cars_photo_form': cars_photo_form
        }



    return render(request, 'cars/add_car.html', {
        'car_form': car_form,
        'cars_photo_form': cars_photo_form
        }) 

@login_required(login_url='login')
def delete_car(request, id):
    user_id = request.user.id
    user = User.objects.get(id = user_id)
    Car.objects.filter(id = id, owner = user).delete()
    messages.success(request, 'Your car was successfully deleted!')

    return redirect('/accounts/user_cars')


@login_required(login_url='login')
def update_car(request, id):
    user_id = request.user.id
    user = User.objects.get(id = user_id)
    car = get_object_or_404(Car, id=id, owner=user_id)
    
    if request.method == 'POST':
        car_form = CarForm(request.POST, instance=car)

        if car_form.is_valid:
            car = car_form.save(commit=False)
            car.save()

            #updating main photo
            if 'car_main_photo' in request.FILES:
                car.car_main_photo = request.FILES['car_main_photo']
                car.save()

                return redirect('cardetails', id = car.id)
            
            return redirect('cardetails', id = car.id)
    else:
        car_form = CarForm(instance=car)

    context = {
        'car_form': car_form,
        'car': car,
    }

    return render(request, 'cars/update_car.html', context)
