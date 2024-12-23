from django.db import models
from donate.models import Donate

class FoodBankStock(models.Model):
    food_name = models.CharField(max_length=100, unique=True)
    total_quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.food_name} - Total Quantity: {self.total_quantity}"

class FoodBankDonation(models.Model):
    donate = models.ForeignKey(Donate, on_delete=models.CASCADE)
    expiry_date = models.DateField()

    def save(self, *args, **kwargs):
        is_new = self.pk is None  # Check if the instance is being created for the first time
        super().save(*args, **kwargs)
        if is_new:
            self.update_food_bank_stock()

    def update_food_bank_stock(self):
        food_name = self.donate.food_name
        donor = self.donate.donor

        total_quantity = FoodBankDonation.objects.filter(donate__donor=donor, donate__food_name=food_name).aggregate(models.Sum('donate__quantity'))['donate__quantity__sum'] or 0

        stock, created = FoodBankStock.objects.get_or_create(food_name=food_name)
        stock.total_quantity = total_quantity
        stock.save()

    def __str__(self):
        return f"{self.donate.food_name} - Quantity: {self.donate.quantity}"

'''from django.db import models
from donate.models import Donate

class FoodBankDonation(models.Model):
    donate = models.ForeignKey(Donate, on_delete=models.CASCADE)
    expiry_date = models.DateField()

    def __str__(self):
        return f"{self.donate.food_name} - Quantity: {self.donate.quantity}"'''