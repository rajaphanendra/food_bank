from django.urls import path
from .views import donate, donation_list

urlpatterns = [
    path('donate/', donate, name='donate'),
    path('donation-list/', donation_list, name='donation_list'),
]
