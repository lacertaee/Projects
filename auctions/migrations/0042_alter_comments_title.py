# Generated by Django 4.1.7 on 2023-04-14 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0041_alter_comments_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]
