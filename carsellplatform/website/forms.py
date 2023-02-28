from django import forms 
from cars.models import Car, CarPhoto


class ContactForm(forms.Form):
    full_name = forms.CharField(
        label = 'Full name',
        max_length=100,
        widget = forms.TextInput(attrs={
            'class': 'form-control full_name',
            'placeholder': 'Full name',
        })
    )

    email = forms.EmailField(
        label = 'Email',
        widget = forms.EmailInput(attrs={
            'class': 'form-control email',
            'placeholder': 'Email',
        })
    )

    subject = forms.CharField(
        label = 'Subject',
        widget = forms.TextInput(attrs={
            'class': 'form-control subject',
            'placeholder': 'Subject',
        })
    )  
    
    phone = forms.CharField(
        label = 'Phone Number',
        widget = forms.TextInput(attrs={
            'class': 'form-control phone',
            'placeholder': 'Phone Number',
        })
    )  

    message = forms.CharField(
        label = 'Message',
        widget = forms.Textarea(attrs={
            'class': 'form-control message',
            'rows': 5,
            'placeholder': 'Enter your message',
        })
    )  
    
