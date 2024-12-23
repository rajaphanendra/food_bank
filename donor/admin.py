from django.contrib import admin
from .models import Donor

class DonorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'mobile_number', 'address', 'ssn', 'date_of_birth')
    search_fields = ['user__username', 'first_name']
    list_filter = ['first_name']

admin.site.register(Donor, DonorAdmin)