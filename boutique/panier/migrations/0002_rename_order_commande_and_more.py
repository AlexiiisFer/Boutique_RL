# Generated by Django 4.2.7 on 2024-06-01 11:07

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_delete_commande'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('panier', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order',
            new_name='Commande',
        ),
        migrations.RenameModel(
            old_name='OrderItem',
            new_name='CommandeArticle',
        ),
    ]