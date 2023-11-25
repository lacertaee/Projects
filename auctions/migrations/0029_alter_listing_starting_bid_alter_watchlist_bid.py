# Generated by Django 4.1.7 on 2023-04-14 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0028_alter_listing_starting_bid_alter_watchlist_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='starting_bid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='auctions.bids'),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='bid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids1', to='auctions.bids'),
        ),
    ]
