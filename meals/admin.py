from django.contrib import admin
from .models import Meals, MealsFoodStock

class MealsFoodStockInline(admin.TabularInline):
    model = MealsFoodStock
    extra = 1

class MealsAdmin(admin.ModelAdmin):
    list_display = ['food_expiry', 'total_meals']
    inlines = [MealsFoodStockInline]

admin.site.register(Meals, MealsAdmin)
admin.site.register(MealsFoodStock)