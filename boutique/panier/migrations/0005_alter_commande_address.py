# Generated by Django 4.2.7 on 2024-06-01 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panier', '0004_rename_date_commande_commande_date_ordered_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
    ]
