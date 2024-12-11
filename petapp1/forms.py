from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import PetUser

class PetUserForm(UserCreationForm):
    class Meta:
        model = PetUser
        fields = ['username', 'fname', 'lname', 'email1', 'phone1', 'address1', 'password1', 'password2']
        """widgets = {
            'username': 'forms.TextInput(attrs:{'class':'form-control'}),
            'fname': forms.TextInput(attrs={'class': 'form-control'}),
            'lname': forms.TextInput(attrs={'class': 'form-control'}),
            'email1': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone1': forms.TextInput(attrs={'class': 'form-control'}),
            'address1': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class':'form-control'}),
            'password2': forms.PasswordInput(attrs={'class':'form-control'}),
        }"""
        