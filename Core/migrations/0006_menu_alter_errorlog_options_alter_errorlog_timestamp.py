# Generated by Django 5.1 on 2024-09-04 20:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0005_alter_errorlog_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование пункта')),
                ('url', models.CharField(max_length=100, verbose_name='Ссылка')),
                ('gk_name', models.CharField(max_length=100, verbose_name='Наименование в GKServer')),
            ],
            options={
                'verbose_name': 'пункт',
                'verbose_name_plural': 'пункты',
            },
        ),
        migrations.AlterModelOptions(
            name='errorlog',
            options={'verbose_name': 'ошибку', 'verbose_name_plural': 'ошибки'},
        ),
        migrations.AlterField(
            model_name='errorlog',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата и время ошибки'),
        ),
    ]
