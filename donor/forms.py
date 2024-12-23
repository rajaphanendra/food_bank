from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Donor
from django.contrib.auth.models import User

class DonorRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    mobile_number = forms.CharField(max_length=15)
    address = forms.CharField(widget=forms.Textarea)
    ssn = forms.CharField(max_length=20, required=True)
    date_of_birth = forms.DateField(help_text='Format: YYYY-MM-DD')

    class Meta:
        model = User  # Use the User model for authentication
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'mobile_number', 'address', 'ssn', 'date_of_birth']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()

        # Create a Donor object and link it to the user
        donor = Donor(user=user,
                      first_name=self.cleaned_data['first_name'],
                      last_name=self.cleaned_data['last_name'],
                      mobile_number=self.cleaned_data['mobile_number'],
                      address=self.cleaned_data['address'],
                      ssn=self.cleaned_data['ssn'],
                      date_of_birth=self.cleaned_data['date_of_birth'])
        donor.save()

        return user