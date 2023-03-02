from django.urls import path
from .views import allcars, cardetails, search, add_car, delete_car, update_car



urlpatterns = [
    path("", allcars, name='cars'),
    path("search", search, name='search'),
    path("add_car", add_car, name='add_car'),
    path("cardetails/<str:id>", cardetails, name='cardetails'),
    path("delete_car/<str:id>", delete_car, name='delete_car'),
    path("update_car/<str:id>", update_car, name='update_car'),
]
