# Generated by Django 4.2.7 on 2024-06-01 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_delete_commande'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produit',
            old_name='category',
            new_name='categorie',
        ),
    ]