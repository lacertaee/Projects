# Generated by Django 4.1.7 on 2023-04-13 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_alter_listing_starting_bid_alter_watchlist_bid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='owner',
        ),
        migrations.AlterField(
            model_name='listing',
            name='starting_bid',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='bid',
            field=models.FloatField(),
        ),
    ]
