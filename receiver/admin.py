from django.contrib import admin
from .models import Receiver

class ReceiverAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'mobile_number', 'address']
    search_fields = ['user__username', 'name']
    list_filter = ['name']

admin.site.register(Receiver, ReceiverAdmin)