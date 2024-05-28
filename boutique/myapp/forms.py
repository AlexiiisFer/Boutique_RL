from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import AdresseFacturation, AdresseLivraison
from django import forms

# Pouvoir changer les informations de l'utilisateur
class UpdateUserForm(UserChangeForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Adresse email'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Prénom'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nom de famille'}))
	password = None

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email',)

	def __init__(self, *args, **kwargs):
		super(UpdateUserForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Pseudo'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>150 caractères ou moins. Seulement lettres, chiffres et @/./+/-/_.</small></span>'

	# Pouvoir changer les informations de l'adresse de facturation 
class UserInfoForm(forms.ModelForm):
	rue = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Rue'}),required=False)
	ville = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ville'}),required=False)
	code_postal = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Code postal'}),required=False)
	pays = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Pays'}),required=False)

	class Meta:
		model = AdresseFacturation
		fields = ('rue', 'ville', 'code_postal', 'pays')

		

# Pouvoir s'inscrire
class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Adresse email'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Prénom'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nom de famille'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Pseudo'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>150 caractères ou moins. Seulement lettres, chiffres et @/./+/-/_.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Mot de passe'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Le mot de passe ne peut ressembler à des infos similaires.</li><li>Le mot de passe doit contenir au moins 8 caractères.</li><li>Le mot de passe ne peut pas contenir que des chiffres.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirmer le mot de passe'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Entrer le même mot de passe.</small></span>'


class AdresseLivraisonForm(forms.ModelForm):
	livraison_titre = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Titre'}), required=False)
	livraison_rue = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Rue'}),required=False)
	livraison_ville = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ville'}),required=False)
	livraison_code_postal = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Code postal'}),required=False)
	livraison_pays = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Pays'}),required=False)

	class Meta:
		model = AdresseLivraison
		fields = ('livraison_titre', 'livraison_rue', 'livraison_ville', 'livraison_code_postal', 'livraison_pays')

		exclude = ['user']
