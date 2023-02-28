from django.urls import path
from .views import allcars, cardetails, search, add_car



urlpatterns = [
    path("", allcars, name='cars'),
    path("search", search, name='search'),
    path("add_car", add_car, name='add_car'),
    path("<str:id>", cardetails, name='cardetails')
]
