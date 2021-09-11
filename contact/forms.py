from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ['email',]
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'full-width', 'placeholder': 'Email: '})
        }
        labels = {
            'email': '',
        }