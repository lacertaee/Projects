# Generated by Django 4.1.7 on 2023-04-14 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0032_bids_bids_bids_owner_delete_winner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bids',
            name='bids',
        ),
        migrations.AddField(
            model_name='bids',
            name='bids',
            field=models.ManyToManyField(blank=True, related_name='bidss', to='auctions.listing'),
        ),
    ]
