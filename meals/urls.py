from django.urls import path
from .views import create_meals, meals_list, staff_login, meals_dashboard, all_requests, staff_logout

urlpatterns = [
    path('create_meals/', create_meals, name='create_meals'),
    path('meals_list/', meals_list, name='meals_list'),
    path('staff_login/', staff_login, name='staff_login'),
    path('staff_logout/', staff_logout, name='staff_logout'),
    path('meals_dashboard', meals_dashboard, name='meals_dashboard'),
    path('all_requests/', all_requests, name='all_requests'),
]
