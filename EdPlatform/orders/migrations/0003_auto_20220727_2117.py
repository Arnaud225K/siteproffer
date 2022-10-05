# Generated by Django 3.2.9 on 2022-07-27 16:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_orderitem_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(default=uuid.UUID('8f37e9b5-0dc7-11ed-8f0d-7c05079056b5'), max_length=250),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(default=uuid.UUID('8f37e9b7-0dc7-11ed-ba2e-7c05079056b5'), max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='postal_code',
            field=models.CharField(default=uuid.UUID('8f37e9b6-0dc7-11ed-997c-7c05079056b5'), max_length=20),
        ),
    ]