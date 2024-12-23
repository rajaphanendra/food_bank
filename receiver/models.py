from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Receiver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name