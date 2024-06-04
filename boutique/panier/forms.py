from django import forms
from .models import Commande


class PaiementForm(forms.Form):
    carte_nom = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Nom sur la carte'}),)
    carte_numero = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Numéro de carte'}))
    carte_date_exp = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Date d\'expiration (MM/AA)'}))
    carte_cvv = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Code CVV'}))


class UserUnlogForm(forms.Form):
    name = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Nom'}),)
    email = forms.EmailField(label='',widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Adresse Email'}))
