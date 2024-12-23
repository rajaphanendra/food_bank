from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Receiver
from django.contrib.auth.models import User

class ReceiverRegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=100)
    mobile_number = forms.CharField(max_length=15)
    address = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User  # Use the User model for authentication
        fields = ['username', 'password1', 'password2', 'name', 'mobile_number', 'address']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()

        # Create a Donor object and link it to the user
        receiver = Receiver(user=user, name=self.cleaned_data["name"], mobile_number=self.cleaned_data["mobile_number"], address=self.cleaned_data["address"])
        receiver.save()

        return user