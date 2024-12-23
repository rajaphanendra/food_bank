from django import forms
from .models import Meals
from foodbankapp.models import FoodBankStock

class MealsForm(forms.ModelForm):
    food_stock = forms.ModelMultipleChoiceField(
        queryset=FoodBankStock.objects.filter(total_quantity__gt=0),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Meals
        fields = ['food_expiry', 'total_meals', 'food_stock']


'''from django import forms
from .models import Meals
from foodbankapp.models import FoodBankStock

class MealsForm(forms.ModelForm):
    food_stock = forms.ModelMultipleChoiceField(
        queryset=FoodBankStock.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Meals
        fields = ['food_expiry', 'total_meals', 'food_stock']'''