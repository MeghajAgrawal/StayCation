from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UpdateUser(forms.ModelForm):
    email=forms.EmailInput()
    class Meta:
        model=User
        fields=['username','email','first_name','last_name']
        widgets={
            'username':forms.TextInput(attrs={'class':'input100', 'name':'username','placeholder':''}),
            'email':forms.EmailInput(attrs={'class':'input100', 'name':'email'}),
            'first_name':forms.TextInput(attrs={'class':'input100', 'name':'first_name'}),
            'last_name':forms.TextInput(attrs={'class':'input100', 'name':'last_name'})
        }
        

class UpdateProfile(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image','dob','age','phone_number']
        widgets={
            'username':forms.TextInput(attrs={'class':'input100', 'name':'username','placeholder':''}),
            'dob':forms.DateInput(attrs={'class':'input100', 'name':'email'}),
            'age':forms.NumberInput(attrs={'class':'input100', 'name':'age'}),
            'phone_number':forms.NumberInput(attrs={'class':'input100', 'name':'phone_number'}),
        }