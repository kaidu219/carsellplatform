from django.shortcuts import render
from rest_framework import generics
from cars.models import Car
from .serializers import CarSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class CarsAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        lst = Car.objects.all().values()
        return Response({'cars': list(lst)})

     


# class CarsAPIView(generics.ListAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer

