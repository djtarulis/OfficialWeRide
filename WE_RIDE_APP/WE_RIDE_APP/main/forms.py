from django import forms
from .models import Sponsor

class SponsorForm(forms.ModelForm):
    class Meta:    
        model = Sponsor
        fields = ['name', 'email', 'phone', 'business_name', 'amount', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'business_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Business Name'}),
            'amount': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'You can leave this as 0 if you are not sure.'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Tell us more about you!.'}),
            }