# Generated by Django 4.2.7 on 2024-03-24 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_produit_is_promo_produit_promo_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]