from django.urls import path
from .views import AllCarsView, CardetailsView, SearchView, CarCreateView, CarDeleteView, UpdateCar



urlpatterns = [
    path("", AllCarsView.as_view(), name='cars'),
    path("search", SearchView.as_view(), name='search'),
    path("add_car", CarCreateView.as_view(), name='add_car'),
    path("cardetails/<str:id>", CardetailsView.as_view(), name='cardetails'),
    path("delete_car/<str:id>", CarDeleteView.as_view(), name='delete_car'),
    path("update_car/<str:id>", UpdateCar.as_view(), name='update_car'),
]
