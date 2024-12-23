from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from .models import FoodBankDonation, FoodBankStock
from .forms import FoodBankDonationForm

def is_staff_or_admin(user):
    return user.is_staff or user.is_admin

class StaffAdminRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not is_staff_or_admin(self.request.user):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class FoodBankDonationListView(StaffAdminRequiredMixin, ListView):
    model = FoodBankDonation
    template_name = 'foodbank/foodbankdonation_list.html'
    context_object_name = 'donations'


class FoodBankDonationCreateView(StaffAdminRequiredMixin, CreateView):
    model = FoodBankDonation
    form_class = FoodBankDonationForm
    template_name = 'foodbank/foodbankdonation_form.html'
    success_url = reverse_lazy('foodbank:donation_list')

    def form_valid(self, form):
        form.instance.update_food_bank_stock()
        return super().form_valid(form)


class FoodBankDonationUpdateView(StaffAdminRequiredMixin, UpdateView):
    model = FoodBankDonation
    form_class = FoodBankDonationForm
    template_name = 'foodbank/foodbankdonation_form.html'
    success_url = reverse_lazy('foodbank:donation_list')

    def form_valid(self, form):
        form.instance.update_food_bank_stock()
        return super().form_valid(form)


class FoodBankDonationDeleteView(StaffAdminRequiredMixin, DeleteView):
    model = FoodBankDonation
    template_name = 'foodbank/foodbankdonation_confirm_delete.html'
    success_url = reverse_lazy('foodbank:donation_list')


def remove_foodbankdonation(request, pk):
    donation = FoodBankDonation.objects.get(pk=pk)
    donation.delete()
    return redirect('foodbank:donation_list')


def foodbank_stock(request):
    stock = FoodBankStock.objects.all()
    return render(request, 'foodbank/foodbank_stock.html', {'stock': stock})
