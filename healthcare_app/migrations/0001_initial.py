# Generated by Django 2.2.13 on 2024-07-01 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=122, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=122, verbose_name='Last Name')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='Username')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email ID')),
                ('address_line1', models.CharField(max_length=255, verbose_name='Address Line 1')),
                ('city', models.CharField(max_length=50, verbose_name='City')),
                ('state', models.CharField(max_length=50, verbose_name='State')),
                ('pincode', models.CharField(max_length=10, verbose_name='Pincode')),
                ('image', models.ImageField(default='default.svg', upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=122, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=122, verbose_name='Last Name')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='Username')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email ID')),
                ('address_line1', models.CharField(max_length=255, verbose_name='Address Line 1')),
                ('city', models.CharField(max_length=50, verbose_name='City')),
                ('state', models.CharField(max_length=50, verbose_name='State')),
                ('pincode', models.CharField(max_length=10, verbose_name='Pincode')),
                ('image', models.ImageField(default='default.svg', upload_to='pics')),
            ],
        ),
    ]