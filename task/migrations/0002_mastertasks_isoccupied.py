# Generated by Django 2.2.11 on 2020-05-07 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mastertasks',
            name='isOccupied',
            field=models.BooleanField(default=False),
        ),
    ]
