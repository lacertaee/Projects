# Generated by Django 4.1.7 on 2023-04-14 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0034_remove_bids_bids_bids_bids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bids',
            name='bids',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bid', to='auctions.listing'),
        ),
    ]