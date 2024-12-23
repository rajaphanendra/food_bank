from django import forms
from .models import Donate

class DonateForm(forms.ModelForm):
    class Meta:
        model = Donate
        fields = ['food_name', 'quantity', 'unit']
