# Generated by Django 5.0 on 2024-03-03 11:11

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('number', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('house_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('area', models.IntegerField()),
                ('floor', models.IntegerField()),
                ('district', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('cost', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('kitchen', models.BooleanField(default=False)),
                ('hall', models.BooleanField(default=False)),
                ('balcany', models.BooleanField(default=False, verbose_name='Balcony')),
                ('desc', models.CharField(max_length=200)),
                ('AC', models.BooleanField(default=False)),
                ('booked', models.BooleanField(default=False, editable=False)),
                ('img', models.ImageField(upload_to='house_id/')),
                ('date', models.DateField(auto_now=True)),
                ('user_email', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('dimention', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('cost', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('kitchen', models.BooleanField(default=False)),
                ('hall', models.BooleanField(default=False)),
                ('balcany', models.BooleanField(default=False, verbose_name='Balcony')),
                ('desc', models.CharField(max_length=200)),
                ('AC', models.BooleanField(default=False)),
                ('booked', models.BooleanField(default=False, editable=False)),
                ('img', models.ImageField(upload_to='room_id/')),
                ('date', models.DateField(auto_now=True)),
                ('user_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('booked', models.BooleanField(default=False)),
                ('date', models.DateField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to=settings.AUTH_USER_MODEL)),
                ('house', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.house')),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.room')),
            ],
        ),
    ]
