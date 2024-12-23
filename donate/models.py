from django.db import models

# Create your models here.
class Donate(models.Model):
    UNIT_CHOICES = [
        ('oz', 'Ounces'),
        ('lb', 'Pounds'),
    ]

    food_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    donor = models.ForeignKey('donor.Donor', on_delete=models.CASCADE)
    date = models.DateField(default='2023-12-07')
    unit = models.CharField(max_length=2, choices=UNIT_CHOICES, default='lb')

    def __str__(self):
        return f"Donation by {self.donor} - {self.food_name}"