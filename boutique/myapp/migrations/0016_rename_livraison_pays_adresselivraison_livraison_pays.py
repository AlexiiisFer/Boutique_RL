# Generated by Django 4.2.7 on 2024-05-28 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_alter_adresselivraison_livraison_pays_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adresselivraison',
            old_name='livraison_Pays',
            new_name='livraison_pays',
        ),
    ]
