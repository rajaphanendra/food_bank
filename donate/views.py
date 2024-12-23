from django.shortcuts import render, redirect
from .models import Donate
from .forms import DonateForm
from django.utils import timezone
from donor.models import Donor
from django.contrib.auth.decorators import login_required

@login_required(login_url='donor_login')
def donate(request):
    if request.method == 'POST':
        form = DonateForm(request.POST)
        print(form.errors)
        if form.is_valid():
            donor = Donor.objects.get(user=request.user)
            donation = form.save(commit=False)

            if form.cleaned_data['food_name'] == 'others':
                donation.food_name = request.POST.get('other_food_name', '')

            donation.donor = donor
            donation.date = timezone.now().date()
            print(timezone.now().date())
            donation.save()
            return redirect('donor_dashboard')
    else:
        form = DonateForm()

    return render(request, 'donate/donate.html', {'form': form})

@login_required(login_url='donor_login')
def donation_list(request):
    donations = Donate.objects.filter(donor__user=request.user).order_by('-date')

    # Group donations by date
    donations_by_date = {}
    for donation in donations:
        date_str = donation.date.strftime('%Y-%m-%d')
        if date_str not in donations_by_date:
            donations_by_date[date_str] = []
        donations_by_date[date_str].append(donation)

    return render(request, 'donate/donation_list.html', {'donations': donations_by_date})
