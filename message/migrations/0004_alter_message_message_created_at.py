# Generated by Django 4.2.2 on 2023-07-26 16:26

from django.db import migrations, models
import django.db.models.functions.datetime


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0003_alter_message_message_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message_created_at',
            field=models.DateTimeField(default=django.db.models.functions.datetime.Now, verbose_name='создано'),
        ),
    ]
