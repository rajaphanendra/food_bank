# urls.py in your foodbank app
from django.urls import path
from .views import FoodBankDonationListView, FoodBankDonationCreateView, FoodBankDonationUpdateView, FoodBankDonationDeleteView, remove_foodbankdonation, foodbank_stock

app_name = 'foodbank'

urlpatterns = [
    path('donations/', FoodBankDonationListView.as_view(), name='donation_list'),
    path('donations/add/', FoodBankDonationCreateView.as_view(), name='donation_add'),
    path('donations/<int:pk>/edit/', FoodBankDonationUpdateView.as_view(), name='donation_edit'),
    path('donations/<int:pk>/delete/', FoodBankDonationDeleteView.as_view(), name='donation_delete'),
    path('donations/<int:pk>/remove/', remove_foodbankdonation, name='donation_remove'),
    path('stock/', foodbank_stock, name='stock'),
]