from django.urls import path
from .views import allcars, cardetails, search



urlpatterns = [
    path("", allcars, name='cars'),
    path("search", search, name='search'),
    path("<str:id>", cardetails, name='cardeteils')
]
