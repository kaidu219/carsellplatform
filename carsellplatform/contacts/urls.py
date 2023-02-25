from django.urls import path
from .views import inquiry, delete_inquiry


urlpatterns = [
    path('inquiry', inquiry, name='inquiry'),
    path("<str:id>", delete_inquiry, name='delete_inquiry')
]
