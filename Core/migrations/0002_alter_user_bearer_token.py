# Generated by Django 5.1 on 2024-09-19 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bearer_token',
            field=models.CharField(default='none', max_length=1000, verbose_name='Bearer Token пользователя'),
        ),
    ]
