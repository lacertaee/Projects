# Generated by Django 4.1.7 on 2023-04-14 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0033_remove_bids_bids_bids_bids'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bids',
            name='bids',
        ),
        migrations.AddField(
            model_name='bids',
            name='bids',
            field=models.FloatField(default=1),
        ),
    ]
