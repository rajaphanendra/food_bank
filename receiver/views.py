from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .forms import ReceiverRegistrationForm
from .models import Receiver
from meals.models import MealsFoodStock

def receiver_register(request):
    if request.method == 'POST':
        form = ReceiverRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user
            print(user)
            login(request, user)
            return redirect('receiver_dashboard')  # Replace with the actual dashboard view name
    else:
        form = ReceiverRegistrationForm()
    return render(request, 'receiver/register.html', {'form': form})

# Similar view for Receiver registration

def receiver_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('receiver_dashboard')  # Replace with the actual dashboard view name
    return render(request, 'receiver/login.html')

def receiver_logout(request):
    logout(request)
    return redirect('receiver_login')

@login_required(login_url='receiver_login')
def receiver_dashboard(request):
    receiver = Receiver.objects.get(user=request.user)

    context = {
        'receiver': receiver,
    }
    return render(request, 'receiver/receiver.html', context)


@login_required(login_url='receiver_login')
def available_meals(request):
    # Get the available meals (where quantity is greater than 0)
    available_meals = MealsFoodStock.objects.filter(quantity__gt=0)

    return render(request, 'receiver/available_meals.html', {'available_meals': available_meals})