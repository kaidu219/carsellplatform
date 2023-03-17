from django.urls import path
from .views import CarsAPIView, CarDetailView, TeamAPIView, TeamDatailView, CarsCreateView

urlpatterns = [
    path('carslist/', CarsAPIView.as_view()),
    path('car/<str:pk>', CarDetailView.as_view()),
    path('carcrate/', CarsCreateView.as_view()),

    path('teamslist/', TeamAPIView.as_view()),
    path('teamslist/<str:pk>', TeamAPIView.as_view()),
    path('worker/<str:pk>', TeamDatailView.as_view()),
]
