from django.urls import path, include
from . import views

urlpatterns = [
    path('donor_register/', views.donor_register, name='donor_register'),
    path('donor_login/', views.donor_login, name='donor_login'),
    path('donor_logout/', views.donor_logout, name='donor_logout'),
    path('donor_dashboard/', views.donor_dashboard, name='donor_dashboard'),
]