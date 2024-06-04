from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Categorie(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Produit(models.Model):
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='images/Produits')
    #Promo
    is_promo = models.BooleanField(default=False,null=True, blank=True)
    promo_price = models.DecimalField(default=0, max_digits=10, decimal_places=2,null=True, blank=True)

    def __str__(self):
        return self.name
        

# Profil utilisateur avec adresse de Facturation
class AdresseFacturation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=1, null=True)
    rue = models.CharField(max_length=255, blank=True)
    ville = models.CharField(max_length=255, blank=True)
    code_postal = models.CharField(max_length=255, blank=True)
    pays = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username
    
  # Création vide du profil avec avec adresse de facturation après que l'utilisateur se soit inscrit  
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = AdresseFacturation(user=instance)
        user_profile.save()

post_save.connect(create_user_profile, sender=User)

# Création vide du profil avec avec adresse de livraison après que l'utilisateur se soit inscrit  
def create_user_livraison(sender, instance, created, **kwargs):
    if created:
        user_livraison = AdresseLivraison(user=instance)
        user_livraison.save()

post_save.connect(create_user_livraison, sender=User)
    
class AdresseLivraison(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    livraison_titre = models.CharField(max_length=255,null=True, blank=True)
    livraison_rue = models.CharField(max_length=255,null=True, blank=True)
    livraison_ville = models.CharField(max_length=255,null=True, blank=True)
    livraison_code_postal = models.CharField(max_length=255,null=True, blank=True)
    livraison_pays = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return self.user.username