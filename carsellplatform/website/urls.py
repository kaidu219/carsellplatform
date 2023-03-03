from django.urls import path
from .views import index, contact, services, AboutView



urlpatterns = [
    path("", index, name='home'),
    path("about/", AboutView.as_view(), name='about'),
    path("contact/", contact, name='contact'),
    path("services/", services, name='services'),
]
