# Generated by Django 4.1.7 on 2023-04-13 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_delete_category_remove_watchlist_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='starting_bid',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='bid',
            field=models.FloatField(default=0),
        ),
    ]
