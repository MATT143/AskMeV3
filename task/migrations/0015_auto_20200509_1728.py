# Generated by Django 2.2.11 on 2020-05-09 11:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0014_auto_20200509_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='mastertasks',
            name='approverComment',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='mastertasks',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 9, 11, 58, 20, 832419, tzinfo=utc)),
        ),
    ]