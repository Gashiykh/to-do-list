# Generated by Django 3.2.25 on 2024-07-17 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20240710_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название проекта')),
                ('description', models.TextField(max_length=500, verbose_name='Описание проекта')),
                ('started_at', models.DateField(verbose_name='Дата начала')),
                ('ended_at', models.DateField(blank=True, null=True, verbose_name='Дата окончания')),
            ],
        ),
    ]