from django.contrib import admin
from .models import FoodBankDonation, FoodBankStock

class FoodBankDonationAdmin(admin.ModelAdmin):
    list_display = ['donate', 'expiry_date']
    search_fields = ['donate__donor__name', 'donate__food_name']

class FoodBankStockAdmin(admin.ModelAdmin):
    list_display = ['food_name', 'total_quantity']

admin.site.register(FoodBankDonation, FoodBankDonationAdmin)
admin.site.register(FoodBankStock, FoodBankStockAdmin)