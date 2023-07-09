# Generated by Django 3.2.20 on 2023-07-09 10:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='ends_at',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='event',
            name='starts_at',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]