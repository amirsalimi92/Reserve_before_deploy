# Generated by Django 4.1.5 on 2023-01-12 15:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.IntegerField(choices=[(1, 'Developers'), (2, 'IT & Product support'), (3, 'Product management'), (4, 'Project leaders'), (5, 'QA'), (6, 'IT infrastructure'), (7, 'Finance & Legal'), (8, 'Marketing'), (9, 'Sell & Solution consulting'), (10, 'HR & people support'), (11, 'Innonspot'), (12, 'Viima'), (13, 'Administration')])),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office', models.IntegerField(choices=[(1, 'Bonn'), (2, 'Cologne'), (3, 'Frankfurt'), (4, 'Other in germany'), (5, 'USA'), (6, 'France'), (7, 'Other')])),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isActive', models.BooleanField(default=True)),
                ('email', models.EmailField(default='@hype.de', max_length=254)),
                ('name', models.CharField(max_length=50)),
                ('family', models.CharField(max_length=60)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='members.department')),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='members.office')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
