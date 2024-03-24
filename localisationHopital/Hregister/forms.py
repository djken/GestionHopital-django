from django import forms
from django.forms import ModelForm
from .models import Hopitaltracker

# Create a Registration form
class HopitalForm(ModelForm):
    class Meta:
        model = Hopitaltracker
        # fields = "__all__"
        
        # fields nous permet de définier nos différents champs de la forme
        fields = ('nom', 'communaute', 'adresse', 'telephone', 'site', 'courriel')
        labels = {
            'nom': '',
            'communaute': '',
            'adresse': '',
            'telephone': '',
            'site': '', 
            'courriel': '',
        }
        
        # Widgets nous permettra de styliser notre forme avec Bootstrap
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hospital Name'}),
            'communaute': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Community'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'site': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wesite Site'}),
            'courriel': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
        }
    