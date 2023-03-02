from django import forms 
from .models import Car, CarPhoto


class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = '__all__'
        exclude = ('owner',)
        widgets = {
            'car_title': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.Select(attrs={'class': 'form-control'}),
            'condition': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'style': 'width: 300px;'}),
            'car_main_photo': forms.FileInput(attrs={'class': 'form-control-file'}),
            'features': forms.SelectMultiple(attrs={'class': 'form-control', 'style': 'height: 250px;'}),
            'body_style': forms.TextInput(attrs={'class': 'form-control'}),
            'engine': forms.TextInput(attrs={'class': 'form-control'}),
            'transmission': forms.TextInput(attrs={'class': 'form-control'}),
            'interior': forms.TextInput(attrs={'class': 'form-control'}),
            'kilometers': forms.NumberInput(attrs={'class': 'form-control'}),
            'doors': forms.TextInput(attrs={'class': 'form-control'}),
            'passengers': forms.NumberInput(attrs={'class': 'form-control'}),
            'vin_no': forms.TextInput(attrs={'class': 'form-control'}),
            'fuel_type': forms.TextInput(attrs={'class': 'form-control'}),
            'no_of_owners': forms.NumberInput(attrs={'class': 'form-control'}),
            'fuel_mileage': forms.TextInput(attrs={'class': 'form-control'}),
            'is_featured': forms.CheckboxInput(attrs={'class': 'form-control-input mx-3'}),
        }
        

class CarPhotoForm(forms.ModelForm):
    class Meta:
        model = CarPhoto
        fields = ['image']
