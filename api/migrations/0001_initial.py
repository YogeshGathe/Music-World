# Generated by Django 4.1 on 2022-09-01 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('singer', models.CharField(max_length=50)),
                ('chord', models.CharField(max_length=10)),
            ],
        ),
    ]
