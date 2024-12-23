from django.db import models
from meals.models import MealsFoodStock
from receiver.models import Receiver

class Request(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Delivered', 'Delivered'),
    ]

    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    meals_food_stock = models.ForeignKey('meals.MealsFoodStock', on_delete=models.CASCADE, default=None, null=True)
    receiver = models.ForeignKey(Receiver, on_delete=models.CASCADE, default=None, null=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        if self.meals_food_stock and hasattr(self.meals_food_stock, 'food_stock') and hasattr(
                self.meals_food_stock.food_stock, 'food_expiry'):
            return f"Request for {self.meals_food_stock.food_stock.food_expiry} - {self.receiver.name}"
        else:
            return f"Request - ID: {self.id} - Status: {self.status}"

    '''def __str__(self):
        return f"Request for {self.meals_food_stock.food_stock.food_expiry} - {self.receiver.name}"'''


'''from django.db import models

# Create your models here.
class Request(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Delivered', 'Delivered'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    meal_expiry = models.DateField()
    receiver = models.ForeignKey('receiver.Receiver', on_delete=models.CASCADE)

    def __str__(self):
        return f"Request for {self.meal_expiry}"'''