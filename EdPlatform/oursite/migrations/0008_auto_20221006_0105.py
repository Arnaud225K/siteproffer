# Generated by Django 3.2 on 2022-10-05 20:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('oursite', '0007_auto_20221006_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constructor',
            name='slug',
            field=models.SlugField(default=uuid.UUID('01610a34-44e9-11ed-8c17-7c05079056b5'), max_length=200),
        ),
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(default=uuid.UUID('016046c2-44e9-11ed-9336-7c05079056b5'), max_length=200),
        ),
        migrations.AlterField(
            model_name='module',
            name='slug',
            field=models.SlugField(default=uuid.UUID('016094f0-44e9-11ed-8ca9-7c05079056b5'), max_length=200),
        ),
    ]
