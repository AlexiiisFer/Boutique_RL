# Generated by Django 4.2.7 on 2024-06-02 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panier', '0011_commande_expedie'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='date_expedie',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
