# Generated by Django 3.2 on 2022-10-05 19:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20220916_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(default=uuid.UUID('ada78588-44e7-11ed-9ea0-7c05079056b5'), max_length=250),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(default=uuid.UUID('ada7858a-44e7-11ed-bbd9-7c05079056b5'), max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='postal_code',
            field=models.CharField(default=uuid.UUID('ada78589-44e7-11ed-b054-7c05079056b5'), max_length=20),
        ),
    ]