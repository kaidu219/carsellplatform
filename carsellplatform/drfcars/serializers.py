from rest_framework import serializers
from cars.models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'car_title', 'state', 'city', 'color', 'model', 'year', 'price', 'condition', 'features', 'body_style', 'engine', 'transmission', 'interior', 'kilometers', 'doors', 'passengers', 'fuel_type', 'no_of_owners', 'fuel_mileage')
        # exclude = ('id', 'owner', 'car_main_photo', 'vin_no', 'is_featured', 'created_date')
        