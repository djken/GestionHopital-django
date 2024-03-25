from django import forms
from django.forms import ModelForm
from .models import Hopitaltracker

# Create a Registration form
class HopitalForm(ModelForm):
    class Meta:
        model = Hopitaltracker
        
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
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom Hopital'}),
            'communaute': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Communauté'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adresse'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telephone'}),
            'site': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Site Web'}),
            'courriel': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Courriel'}),
        }
    