# Generated by Django 4.1.7 on 2023-04-10 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_listing_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='starting_bid',
            field=models.FloatField(),
        ),
    ]
