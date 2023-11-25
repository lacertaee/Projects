# Generated by Django 4.1.7 on 2023-04-14 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0025_alter_listing_starting_bid_alter_watchlist_bid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.FloatField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='listing',
            name='starting_bid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='auctions.bids'),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='bid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bids1', to='auctions.bids'),
        ),
    ]
