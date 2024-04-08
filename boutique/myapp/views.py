from django.shortcuts import render, redirect
from .models import Produit, Categorie
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms

# Create your views here.

def home(request):
    categories = Produit.objects.values_list('category', flat=True).distinct()

    # Initialiser une liste pour stocker un produit par catégorie
    unique_produits = []

    # Pour chaque catégorie, récupérer un seul produit de cette catégorie
    for category in categories:
        produit = Produit.objects.filter(category=category).first()
        if produit:
            unique_produits.append(produit)

    context = {
        'unique_produits': unique_produits,
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def boutique(request):
    return render(request, 'boutique.html')

def produit(request, pk):
    produit = Produit.objects.get(id=pk)
    return render(request, 'produit.html', {'produit': produit})



def product_list(request):
    produits = Produit.objects.all()
    categories = Categorie.objects.all()

    # Filtrage par catégorie
    category = request.GET.get('category')
    if category:
        produits = produits.filter(category=Categorie.objects.get(name=category))

    # Recherche par nom spécifique
    query = request.GET.get('q')
    if query:
        produits = produits.filter(name__icontains=query)

    context = {
        'produits': produits,
        'categories': categories,
    }
    return render(request, 'boutique.html', context)








def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Vous êtes connecté")
            return redirect('home')
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect")
    return render(request, 'login.html')

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "Vous êtes connecté")
            return redirect('home')
        else:
            messages.error(request, "Erreur lors de l'inscription")
            return redirect('register')
    else:
        return render(request, 'register.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.error(request, "Vous êtes déconnecté")
    return redirect('home')

def profile(request):
    return render(request, 'profile.html')