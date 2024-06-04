from django.db import models
from django.contrib.auth.models import User
from myapp.models import Produit
from django.db.models.signals import pre_save
from django.dispatch import receiver
import datetime

# Create your models here.

class Commande (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    address = models.TextField(max_length=15000)
    date_ordered = models.DateTimeField(auto_now_add=True)
    prix_total = models.DecimalField(max_digits=10, decimal_places=2,)
    expedie = models.BooleanField(default=False)
    date_expedie = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'Commande n°{str(self.id)}'

@receiver(pre_save, sender=Commande)
def set_date_expedie(sender, instance, **kwargs):
    if instance.pk:
        now = datetime.datetime.now()
        obj = sender._default_manager.get(pk=instance.pk)
        if instance.expedie and not obj.expedie:
            instance.date_expedie = now
       


class CommandeArticle(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantitee = models.PositiveBigIntegerField(default=1)
    prix = models.DecimalField(max_digits=10, decimal_places=2,)

    def __str__(self):
        return f'Commande Article n°{str(self.id)}'
    
