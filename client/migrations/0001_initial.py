# Generated by Django 4.2.2 on 2023-07-27 18:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_second_name', models.CharField(max_length=50, verbose_name='фамилия')),
                ('client_first_name', models.CharField(max_length=50, verbose_name='имя')),
                ('client_surname', models.CharField(blank=True, max_length=50, null=True, verbose_name='отчество')),
                ('client_email', models.EmailField(max_length=254, verbose_name='почта')),
                ('client_comments', models.TextField(blank=True, null=True, verbose_name='комментарии')),
                ('client_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'клиент',
                'verbose_name_plural': 'клиенты',
                'ordering': ('client_second_name',),
            },
        ),
    ]
