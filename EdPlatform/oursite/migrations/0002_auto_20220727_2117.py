# Generated by Django 3.2.9 on 2022-07-27 16:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oursite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('D', 'Dialog'), ('C', 'Chat')], default='D', max_length=1, verbose_name='Тип')),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Участник')),
            ],
        ),
        migrations.AlterField(
            model_name='constructor',
            name='slug',
            field=models.SlugField(default=uuid.UUID('8f367633-0dc7-11ed-9c4a-7c05079056b5'), max_length=200),
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(default=uuid.UUID('8f355101-0dc7-11ed-93b9-7c05079056b5'), max_length=200),
        ),
        migrations.AlterField(
            model_name='module',
            name='slug',
            field=models.SlugField(default=uuid.UUID('8f35b2b1-0dc7-11ed-883a-7c05079056b5'), max_length=200),
        ),
        migrations.AlterField(
            model_name='module',
            name='video',
            field=models.ImageField(upload_to='video/'),
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/%Y/%m/%d')),
                ('title', models.CharField(max_length=200)),
                ('clickbait', models.TextField()),
                ('overview', models.TextField()),
                ('url', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата уведомления')),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата сообщения')),
                ('is_readed', models.BooleanField(default=False, verbose_name='Прочитано')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oursite.chat', verbose_name='Чат')),
            ],
            options={
                'ordering': ['pub_date'],
            },
        ),
        migrations.CreateModel(
            name='ImageForUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/%Y/%m/%d')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userPic', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
