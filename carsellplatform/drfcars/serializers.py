from rest_framework import serializers
from cars.models import Car
from uaccounts.models import Comment
from website.models import Team

from django.contrib.auth.models import User


class CarSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(slug_field=User.USERNAME_FIELD, read_only=True)
    class Meta:
        model = Car
        fields = ('id', 'owner', 'car_title', 'state', 'description', 'city', 'color', 'model', 'year', 'price', 'condition', 'features', 'body_style', 'engine', 'transmission', 'interior', 'kilometers', 'doors', 'passengers', 'fuel_type', 'no_of_owners', 'fuel_mileage','vin_no',)
        # exclude = ('id', 'owner', 'car_main_photo', 'vin_no', 'is_featured', 'created_date')
        
class CarDetailViewSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(slug_field=User.USERNAME_FIELD, read_only=True)
    class Meta:
        model = Car
        exclude = ('car_main_photo', 'created_date', 'is_featured', 'vin_no')

def validate_features(value_list):
    allowed_options = [option[0] for option in Car.featured_options]
    invalid_values = [value for value in value_list if value not in allowed_options]

    if invalid_values:
        raise serializers.ValidationError(f"invalid feature value: {', '.join(invalid_values)} ")
    return value_list


class CarCreateSerializer(serializers.ModelSerializer):
    features = serializers.ListField(child=serializers.CharField(), validators=[validate_features])
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

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class CommentDetailViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

# class CommentSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Comment
#         fields = "__all__"

