# Generated by Django 4.1 on 2022-08-24 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]