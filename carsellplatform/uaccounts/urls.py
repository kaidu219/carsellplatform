from django.urls import path
from .views import login, logout, register, DashboardView, user_cars



urlpatterns = [
    path("login", login, name='login'),
    path("logout", logout, name='logout'),
    path("register", register, name='register'),
    path("dashboard", DashboardView.as_view(), name='dashboard'),
    path("user_cars", user_cars, name='user_cars'),
]
