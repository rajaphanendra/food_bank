from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .forms import DonorRegistrationForm
from .models import Donor

def donor_register(request):
    if request.method == 'POST':
        form = DonorRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user
            print(user)
            login(request, user)
            return redirect('donor_dashboard')  # Replace with the actual dashboard view name
    else:
        form = DonorRegistrationForm()
    return render(request, 'donor/register.html', {'form': form})

# Similar view for Receiver registration

def donor_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print(f"User {username} authenticated successfully.")
            return redirect('donor_dashboard')  # Replace with the actual dashboard view name
        else:
            print(f"User {username} authentication failed.")
    return render(request, 'donor/login.html')

def donor_logout(request):
    logout(request)
    return redirect('donor_login')

@login_required(login_url='donor_login')
def donor_dashboard(request):
    donor = Donor.objects.get(user=request.user)

    context = {
        'donor': donor,
    }
    return render(request, 'donor/donor.html', context)