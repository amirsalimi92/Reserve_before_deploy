# Generated by Django 4.1.5 on 2023-01-17 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Office', '0004_bugreport'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bugreport',
            name='reporter',
        ),
    ]