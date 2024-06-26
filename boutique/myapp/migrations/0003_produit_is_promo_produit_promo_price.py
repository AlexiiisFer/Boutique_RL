# Generated by Django 4.2.7 on 2024-03-24 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_categories_categorie_rename_clients_client_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='is_promo',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='produit',
            name='promo_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
