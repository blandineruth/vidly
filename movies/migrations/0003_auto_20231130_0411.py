# Generated by Django 3.2 on 2023-11-30 04:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_year',
            field=models.CharField(max_length=225),
        ),
    ]
