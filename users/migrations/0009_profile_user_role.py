# Generated by Django 2.2.11 on 2020-05-09 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_role',
            field=models.CharField(choices=[('approver', 'APPROVER'), ('consultant', 'CONSULTANT'), ('select role', 'SELECT ROLE')], default='select role', max_length=30),
        ),
    ]