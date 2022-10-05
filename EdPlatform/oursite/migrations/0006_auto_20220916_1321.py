# Generated by Django 3.2.9 on 2022-09-16 08:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('oursite', '0005_auto_20220802_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constructor',
            name='slug',
            field=models.SlugField(default=uuid.UUID('82a57679-3598-11ed-87c5-7c05079056b5'), max_length=200),
        ),
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(default=uuid.UUID('82a416b2-3598-11ed-9cd9-7c05079056b5'), max_length=200),
        ),
        migrations.AlterField(
            model_name='module',
            name='slug',
            field=models.SlugField(default=uuid.UUID('82a48bf1-3598-11ed-b55f-7c05079056b5'), max_length=200),
        ),
    ]