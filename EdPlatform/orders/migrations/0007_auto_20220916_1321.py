# Generated by Django 3.2.9 on 2022-09-16 08:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20220802_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(default=uuid.UUID('82ac07cb-3598-11ed-8623-7c05079056b5'), max_length=250),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(default=uuid.UUID('82ac07cd-3598-11ed-af4a-7c05079056b5'), max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='postal_code',
            field=models.CharField(default=uuid.UUID('82ac07cc-3598-11ed-8bcc-7c05079056b5'), max_length=20),
        ),
    ]
