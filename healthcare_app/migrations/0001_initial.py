# Generated by Django 2.2.13 on 2024-07-07 06:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=122, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=122, verbose_name='Last Name')),
                ('username', models.CharField(max_length=50, verbose_name='Username')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email ID')),
                ('address_line1', models.CharField(max_length=255, verbose_name='Address Line 1')),
                ('city', models.CharField(max_length=50, verbose_name='City')),
                ('state', models.CharField(max_length=50, verbose_name='State')),
                ('pincode', models.CharField(max_length=10, verbose_name='Pincode')),
                ('image', models.ImageField(default='default.svg', upload_to='pics')),
                ('is_doctor', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(default=uuid.uuid4, editable=False, max_length=50, unique=True, verbose_name='Blog Number')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('image', models.ImageField(blank=True, null=True, upload_to='pics', verbose_name='Image')),
                ('category', models.CharField(max_length=50, verbose_name='Category')),
                ('summary', models.TextField(verbose_name='Summary')),
                ('content', models.TextField(verbose_name='Content')),
                ('draft', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to='healthcare_app.Users')),
            ],
        ),
    ]
