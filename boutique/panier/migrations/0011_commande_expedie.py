# Generated by Django 4.2.7 on 2024-06-01 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panier', '0010_rename_quantite_commandearticle_quantitee_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='expedie',
            field=models.BooleanField(default=False),
        ),
    ]
