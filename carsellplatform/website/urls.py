from django.urls import path
from .views import IndexView, ContactView, AboutView, SevicesView



urlpatterns = [
    path("", IndexView.as_view(), name='home'),
    path("about/", AboutView.as_view(), name='about'),
    path("contact/", ContactView.as_view(), name='contact'),
    path("services/", SevicesView.as_view(), name='services'),
]
