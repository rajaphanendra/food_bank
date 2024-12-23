# admin.py in the request app

from django.contrib import admin
from .models import Request

class RequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'meals_expiry', 'receiver_name', 'quantity']

    def meals_expiry(self, obj):
        return obj.meals_food_stock.meals.food_expiry if obj.meals_food_stock and obj.meals_food_stock.meals else None

    def receiver_name(self, obj):
        return obj.receiver.name if obj.receiver else None

admin.site.register(Request, RequestAdmin)
