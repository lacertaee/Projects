# Generated by Django 4.1.7 on 2023-04-13 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_category_alter_listing_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='category',
        ),
    ]
