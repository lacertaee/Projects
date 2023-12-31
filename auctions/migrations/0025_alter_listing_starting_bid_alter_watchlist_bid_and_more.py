# Generated by Django 4.1.7 on 2023-04-14 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0024_bids_bid_alter_listing_starting_bid_and_more'),
    ]

    operations = [
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
        migrations.DeleteModel(
            name='bids',
        ),
    ]
