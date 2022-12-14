# Generated by Django 3.2.9 on 2022-07-27 17:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('oursite', '0002_auto_20220727_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constructor',
            name='slug',
            field=models.SlugField(default=uuid.UUID('b30f6d5a-0dcf-11ed-9e41-7c05079056b5'), max_length=200),
        ),
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(default=uuid.UUID('b30e5bc1-0dcf-11ed-b01f-7c05079056b5'), max_length=200),
        ),
        migrations.AlterField(
            model_name='module',
            name='slug',
            field=models.SlugField(default=uuid.UUID('b30ed0f9-0dcf-11ed-8126-7c05079056b5'), max_length=200),
        ),
    ]
