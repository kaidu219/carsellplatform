from django.urls import path
from .views import *

urlpatterns = [
    path('carslist/', CarsAPIView.as_view()),
    path('car/<str:pk>', CarDetailView.as_view()),
    path('carcreate/', CarsCreateView.as_view()),
    path('carupdate/<str:pk>', CarUpdateAPIView.as_view()),
    path('cardelete/<str:pk>', CarDeleteAPIView.as_view()),

    path('teamslist/', TeamAPIView.as_view()),
    path('teamslist/<str:pk>', TeamAPIView.as_view()),
    path('worker/<str:pk>', TeamDatailView.as_view()),
    path('workerdelete/<str:pk>', TeamDeleteAPIView.as_view()),

    path('commentsslist/', CommentAPIView.as_view()),
    path('comment/<str:pk>', CommentDetailView.as_view()),
    path('commentsslist/<str:pk>', CommentAPIView.as_view()),
    path('commentdelete/<str:pk>', CommentDeleteAPIView.as_view()),
]
