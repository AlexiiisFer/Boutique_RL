from django.contrib import admin
from .models import Categorie, Produit, Commande, AdresseFacturation, AdresseLivraison
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(Categorie)
admin.site.register(Produit)
admin.site.register(Commande)
admin.site.register(AdresseFacturation)
admin.site.register(AdresseLivraison)



# Fonctionnalité qui permet d'ajouter le profil (AdresseFacturation) de l'utilisateur
class Profileinline(admin.StackedInline):
    model = AdresseFacturation
    can_delete = False
    verbose_name_plural = 'AdresseFacturation'

class UserAdmin(admin.ModelAdmin):
    model = User
    field = ['username', 'email', 'first_name', 'last_name', 'password']
    inlines = (Profileinline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)