from django.urls import path, include
from . import views

urlpatterns = [
    path('receiver_register/', views.receiver_register, name='receiver_register'),
    path('receiver_login/', views.receiver_login, name='receiver_login'),
    path('receiver_logout/', views.receiver_logout, name='receiver_logout'),
    path('receiver_dashboard/', views.receiver_dashboard, name='receiver_dashboard'),
    path('available_meals/', views.available_meals, name='available_meals'),
]