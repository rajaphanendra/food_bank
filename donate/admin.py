from django.contrib import admin
from .models import Donate

class DonateAdmin(admin.ModelAdmin):
    list_display = ['donor', 'food_name', 'quantity']
    search_fields = ['donor__name', 'food_name']

admin.site.register(Donate, DonateAdmin)
