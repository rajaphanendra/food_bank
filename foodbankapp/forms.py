from django import forms
from .models import FoodBankDonation

class FoodBankDonationForm(forms.ModelForm):
    class Meta:
        model = FoodBankDonation
        fields = ['donate', 'expiry_date']

    def clean_donate(self):
        donate = self.cleaned_data['donate']
        if FoodBankDonation.objects.filter(donate=donate).exists():
            raise forms.ValidationError("This donation is already in the food bank.")
        return donate
