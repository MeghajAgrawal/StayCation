from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    email=forms.EmailInput()
    class Meta:
        model=Contact
        fields=['full_name','email','message']
        widgets={
            'full_name':forms.TextInput(attrs={'class':'form-control', 'name':'fullname','placeholder':''}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'name':'email'}),
            'message':forms.TextInput(attrs={'class':'form-control', 'name':'message'}),
        }