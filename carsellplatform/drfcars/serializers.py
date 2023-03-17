from rest_framework import serializers
from cars.models import Car
from uaccounts.models import Comment
from website.models import Team

from django.contrib.auth.models import User


class CarSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(slug_field=User.USERNAME_FIELD, read_only=True)
    class Meta:
        model = Car
        fields = ('id', 'owner', 'car_title', 'state', 'city', 'color', 'model', 'year', 'price', 'condition', 'features', 'body_style', 'engine', 'transmission', 'interior', 'kilometers', 'doors', 'passengers', 'fuel_type', 'no_of_owners', 'fuel_mileage')
        # exclude = ('id', 'owner', 'car_main_photo', 'vin_no', 'is_featured', 'created_date')
        
class CarDetailViewSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(slug_field=User.USERNAME_FIELD, read_only=True)
    class Meta:
        model = Car
        exclude = ('car_main_photo', 'created_date', 'is_featured', 'vin_no')


class CarCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        exclude = ('car_main_photo',)


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class TeamDetailViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'first_name', 'last_name', 'designation')


# class CommentSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Comment
#         fields = "__all__"

