from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import Meals
from .forms import MealsForm
from django.contrib.auth.decorators import login_required, user_passes_test
from request.models import Request


def staff_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('create_meals')  # Replace with the actual dashboard view name
    return render(request, 'meals/login.html')

def staff_logout(request):
    logout(request)
    return redirect('staff_login')


def is_staff_or_admin(user):
    return user.is_staff or user.is_admin

@login_required(login_url='staff_login')
@user_passes_test(is_staff_or_admin, login_url='staff_login')
def create_meals(request):
    if request.method == 'POST':
        form = MealsForm(request.POST)
        if form.is_valid():
            meals_instance = form.save(commit=False)
            tm = meals_instance.total_meals
            if tm > 0:
                print('meals_instance : ', meals_instance)
                meals_instance.save()
                meals_instance.create_meals(form)
                l = Meals.objects.filter(total_meals=0).last()
                lpk = l.pk
                print('last prim_key: ', lpk)
                print('total_meal: ', tm)
                Meals.objects.filter(id=lpk).update(total_meals=tm)
                return redirect('meals_list')
    else:
        form = MealsForm()

    return render(request, 'meals/create_meals.html', {'form': form})

@login_required(login_url='staff_login')
@user_passes_test(is_staff_or_admin, login_url='staff_login')
def meals_list(request):
    meals_list = Meals.objects.all()
    #print(meals_list)
    #for meal in meals_list:
    #    print(meal)
    return render(request, 'meals/meals_list.html', {'meals_list': meals_list})


@login_required(login_url='staff_login')
@user_passes_test(is_staff_or_admin, login_url='staff_login')
def meals_dashboard(request):
    return render(request, 'meals/meals_dashboard.html')


@login_required(login_url='staff_login')
@user_passes_test(is_staff_or_admin, login_url='staff_login')
def all_requests(request):
    requests = Request.objects.all()
    return render(request, 'meals/all_requests.html', {'requests': requests})