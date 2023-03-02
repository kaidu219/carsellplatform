import uuid
from django.db import models
from datetime import datetime
from multiselectfield import MultiSelectField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Create your models here.
class Car(models.Model):
    state_choice = (
        ('FRU', 'Bishkek'),
        ('CH', 'Chuy'),
        ('OSH', 'Osh'),
        ('NN', 'Naryn'),
        ('IK', 'Issyk Kul'),
        ('JA', 'Jalal Abad'),
        ('BN', 'Batken'),
        ('TS', 'Talas'),
    )

    featured_options = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('Parking Assist', 'Parking Assist'),
        ('Video Camera', 'Video Camera'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
        ('Auto Pilot', 'Auto Pilot'),
        ('ABS', 'ABS'),
        ('Luke', 'Luke'),
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    year_choise = [(r, r) for r in range(2000, (datetime.now().year + 1))]
    year_choise = tuple(year_choise)
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    car_title = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cars', null=True, blank=True)
    state = models.CharField(choices=state_choice, max_length=100)
    city = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField(('year'), choices=year_choise)
    condition = models.CharField(max_length=255)
    price = models.IntegerField()
    description = RichTextField()
    car_main_photo = models.ImageField(upload_to='photos/cars/%Y/%m/%d/', null=True, blank=True)
    features = MultiSelectField(choices=featured_options, max_length=255)
    body_style = models.CharField(max_length=255)
    engine = models.CharField(max_length=255)
    transmission = models.CharField(max_length=255)
    interior = models.CharField(max_length=255)
    kilometers = models.IntegerField()
    doors = models.CharField(max_length=255)
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=255)
    fuel_type = models.CharField(max_length=255)
    no_of_owners = models.IntegerField()
    fuel_mileage = models.CharField(max_length=255)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return self.car_title
    
    class Meta:
        ordering = ['created_date']
    

class CarPhoto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    car_photo = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, blank=True)
    image = models.FileField(upload_to = 'photos/cars/car_photos/%Y/%m/%d/')
   
    def __str__(self) -> str:
        return self.car_photo.car_title
    
    class Meta:
        verbose_name = 'Car photo'
        verbose_name_plural = 'Car photos'