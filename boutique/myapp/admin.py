from django.contrib import admin
from .models import Categorie, Produit, Client, Commande

# Register your models here.

admin.site.register(Categorie)
admin.site.register(Produit)
admin.site.register(Client)
admin.site.register(Commande)