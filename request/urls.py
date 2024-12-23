from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.request_food, name='request_food'),
    path('request_list/', views.request_list, name='request_list'),
]