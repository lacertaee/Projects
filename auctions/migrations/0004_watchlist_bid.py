# Generated by Django 4.1.7 on 2023-04-08 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_watchlist_alter_listing_category_alter_listing_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='bid',
            field=models.IntegerField(default=0),
        ),
    ]
