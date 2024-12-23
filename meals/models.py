from django.db import models
from foodbankapp.models import FoodBankStock
from django.db.models import F

class Meals(models.Model):
    food_expiry = models.DateField()
    total_meals = models.PositiveIntegerField()

    def create_meals(self, form):
        food_quantities = form.cleaned_data['food_stock']
        print(food_quantities)

        # Calculate total quantity to be reduced
        print('total_meals before total_quantity_to_reduce: ', self.total_meals)
        total_quantity_to_reduce = min(self.total_meals,
                                       sum(food_quantity.total_quantity for food_quantity in food_quantities))

        for food_quantity in food_quantities:
            print(food_quantity)
            print('food_quantity.total_quantity: ', food_quantity.total_quantity)
            quantity_taken = min(food_quantity.total_quantity, total_quantity_to_reduce)

            # Reduce FoodBankStock quantity
            print('Reduce FoodBankStock entering')
            print('quantity_taken: ', quantity_taken)
            food_quantity.total_quantity -= quantity_taken
            print('food_quantity.total_quantity before save: ', food_quantity.total_quantity)
            food_quantity.save()

            # Create MealsFoodStock
            print('Create MealsFoodStock entering')
            meals_food_stock = MealsFoodStock(meals=self, food_stock=food_quantity, quantity=quantity_taken)
            print('meals_food_stock: ', meals_food_stock)
            meals_food_stock.save()

            # Reduce total meals count
            print('Reduce total meals count entering')
            print('total_meals before reducing the quantity_taken: ', self.total_meals)
            #self.total_meals -= quantity_taken

            if self.total_meals > 0:
                #break
                self.total_meals -= quantity_taken

        # Save the updated Meals object
        self.save()

    def __str__(self):
        return f"Meals for {self.food_expiry}"

class MealsFoodStock(models.Model):
    meals = models.ForeignKey(Meals, on_delete=models.CASCADE)
    food_stock = models.ForeignKey(FoodBankStock, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


    def __str__(self):
        return f"{self.meals.food_expiry} - {self.food_stock.food_name} - Quantity: {self.quantity}"

    '''def save(self, *args, **kwargs):
        # Update the quantity of the related FoodBankStock
        self.food_stock.total_quantity -= self.quantity
        self.food_stock.save()

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Restore the quantity of the related FoodBankStock if the MealsFoodStock is deleted
        self.food_stock.total_quantity += self.quantity
        self.food_stock.save()

        super().delete(*args, **kwargs)'''


'''
class Meals(models.Model):
    food_expiry = models.DateField()
    total_meals = models.PositiveIntegerField()

    def create_meals(self):
        food_quantities = FoodBankStock.objects.filter(total_quantity__gt=0).order_by('food_name', 'total_quantity')

        for food_quantity in food_quantities:
            if food_quantity.total_quantity > 0:
                quantity_taken = min(food_quantity.total_quantity, self.total_meals)

                # Use F objects for atomic update
                updated_rows = FoodBankStock.objects.filter(
                    id=food_quantity.id,
                    total_quantity__gte=quantity_taken
                ).update(total_quantity=F('total_quantity') - quantity_taken)

                if updated_rows > 0:
                    # Create MealsFoodStock
                    meals_food_stock = MealsFoodStock(meals=self, food_stock=food_quantity, quantity=quantity_taken)
                    meals_food_stock.save()

                    # Reduce total meals count
                    self.total_meals -= quantity_taken

                    if self.total_meals <= 0:
                        break

        # Update Meals with the list of food
        self.save()

    def __str__(self):
        return f"Meals for {self.food_expiry}"

class MealsFoodStock(models.Model):
    meals = models.ForeignKey(Meals, on_delete=models.CASCADE)
    food_stock = models.ForeignKey(FoodBankStock, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.meals.food_expiry} - {self.food_stock.food_name} - Quantity: {self.quantity}"'''







'''from django.db import models
from foodbankapp.models import FoodBankStock, FoodBankDonation

class Meals(models.Model):
    food_expiry = models.DateField()
    total_meals = models.PositiveIntegerField()
    list_of_food = models.ManyToManyField(FoodBankStock, through='MealsFoodStock')

    def create_meals(self):
        food_quantities = FoodBankStock.objects.filter(total_quantity__gt=0).order_by('food_name', 'total_quantity')
        meals = []

        for food_quantity in food_quantities:
            if food_quantity.total_quantity > 0:
                quantity_taken = min(food_quantity.total_quantity, self.total_meals)

                # Update MealsFoodStock
                meals_food_stock = MealsFoodStock(meals=self, food_stock=food_quantity, quantity=quantity_taken)
                meals_food_stock.save()

                # Reduce total meals count
                self.total_meals -= quantity_taken

                if self.total_meals <= 0:
                    break

        # Update Meals with the list of food
        self.save()

    def __str__(self):
        return f"Meals for {self.food_expiry}"

class MealsFoodStock(models.Model):
    meals = models.ForeignKey(Meals, on_delete=models.CASCADE)
    food_stock = models.ForeignKey(FoodBankStock, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.meals.food_expiry} - {self.food_stock.food_name} - Quantity: {self.quantity}"'''

'''from django.db import models
from foodbankapp.models import FoodBankDonation, FoodBankStock

class Meals(models.Model):
    food_expiry = models.DateField()
    total_meals = models.PositiveIntegerField()
    list_of_food = models.JSONField()

    def create_meals(self):
        food_quantities = FoodBankStock.objects.all().order_by('food_name', 'total_quantity')
        meals = []

        for food_quantity in food_quantities:
            if food_quantity.total_quantity > 0:
                food_name = food_quantity.food_name
                quantity_taken = min(food_quantity.total_quantity, self.total_meals)

                meals.append({
                    'food_name': food_name,
                    'quantity': quantity_taken,
                    'expiry_date': self.food_expiry,
                })

                # Update FoodBankStock
                food_quantity.total_quantity -= quantity_taken
                food_quantity.save()

                # Reduce total meals count
                self.total_meals -= quantity_taken

                if self.total_meals <= 0:
                    break

        # Update Meals with the list of food
        self.list_of_food = meals
        self.save()

    def __str__(self):
        return f"Meals for {self.food_expiry}"'''


'''from django.db import models

# Create your models here.
class Meals(models.Model):
    food_expiry = models.DateField()
    total_meals = models.PositiveIntegerField()
    list_of_food = models.JSONField()

    def __str__(self):
        return f"Meals for {self.food_expiry}"'''
