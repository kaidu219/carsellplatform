from django.db import models
from django.contrib.auth.models import User
import uuid
from cars.models import Car

# Create your models here.

class Comment(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, null=False, unique=True, editable=False)
    car = models.ForeignKey(Car, related_name='comments', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name} commented on {self.car.car_title}'


