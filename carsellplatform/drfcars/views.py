from django.shortcuts import render
from django.forms import model_to_dict

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from cars.models import Car
from website.models import Team
from uaccounts.models import Comment
from .serializers import *


# methods for Cars
class CarsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)
    
class CarsCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CarCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # lst = Car.objects.all().values()
        # return Response({'cars': list(lst)})

    # def post(self, request, format=None):
    #     return Response({'title': 'Ferrari f1'})
     
class CarDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        car = Car.objects.get(pk=pk)
        serializer = CarDetailViewSerializer(car)
        return Response(serializer.data)

class CarUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        car = Car.objects.get(pk=pk)
        serializer = CarCreateSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CarDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        car = Car.objects.get(pk=pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# methods for team
class TeamAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        team = Team.objects.all()
        serializer = TeamSerializer(team, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        team = TeamSerializer(data=request.data)
        if team.is_valid():
            team.save()
            return Response(team.data)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "Method PUT not allowed!"})
        try:
            isinstance = Team.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist!"})

        serializer = TeamSerializer(data=request.data, instance=isinstance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class TeamDatailView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk):
        worker = Team.objects.get(id=pk)
        serializer = TeamDetailViewSerializer(worker)
        return Response(serializer.data)
    
class TeamDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, pk):
        worker = Team.objects.filter(pk=pk)
        worker.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# methods for comment
class CommentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "Method PUT not allowed!"})
        try:
            isinstance = Comment.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist!"})

        serializer = CommentSerializer(data=request.data, instance=isinstance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class CommentDetailView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        serializer = CommentDetailViewSerializer(comment)
        return Response(serializer.data)
    
class CommentDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, pk):
        comment = Comment.objects.filter(pk=pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# class TeamAPIView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request, format=None):
#         lst = Team.objects.all().values()
#         return Response({'workers': list(lst)})
    
#     def post(self, request, format=None):
#         team_create = Team.objects.create(
#             first_name = request.data['first_name'],
#             last_name = request.data['last_name'],
#             designation = request.data['designation'],
#         )
#         return Response({'team': model_to_dict(team_create)})

# class CarsAPIView(generics.ListAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer

# class CommentAPIView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request, pk):
#         comment = Comment.objects.all()
#         serializer = CommentSerializer(comment)

#         return Response(serializer.data)