# Generated by Django 5.0 on 2024-03-03 14:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='number',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(10)]),
        ),
    ]
