# Generated by Django 2.2.11 on 2020-05-09 09:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0012_auto_20200509_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mastertasks',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 9, 9, 55, 54, 210640, tzinfo=utc)),
        ),
    ]
