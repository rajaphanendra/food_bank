from django import forms

class RequestForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, label='Quantity')