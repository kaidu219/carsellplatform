from django.db import models
import uuid

class Contact(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    car_id = models.CharField(max_length=500)
    car_title = models.CharField(max_length=200)
    customer_need = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    user_id = models.CharField(max_length=100, blank=True)
    created_date = models.DateTimeField(blank=True, auto_now_add=True)


    def __str__(self) -> str:
        return self.email
    
