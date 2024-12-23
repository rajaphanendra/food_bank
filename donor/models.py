from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=30, default='smith')
    mobile_number = models.CharField(max_length=15)
    address = models.TextField()
    ssn = models.CharField(max_length=9, default='12345789')
    date_of_birth = models.DateField(default='2000-01-01')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"