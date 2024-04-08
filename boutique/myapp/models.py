from django.db import models
import datetime

# Create your models here.

class Categorie(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Produit(models.Model):
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='images/Produits')
    #Promo
    is_promo = models.BooleanField(default=False)
    promo_price = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name
    
class Commande(models.Model):
    product = models.ForeignKey(Produit, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateField(default=datetime.datetime.now)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product.name
