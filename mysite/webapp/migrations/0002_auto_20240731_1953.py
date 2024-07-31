# Generated by Django 3.2.25 on 2024-07-31 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0001_initial'),
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
        migrations.RemoveField(
            model_name='task',
            name='type',
        ),
        migrations.AddField(
            model_name='task',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='tasks', to='webapp.status', verbose_name='Статус'),
        ),
        migrations.CreateModel(
            name='TaskType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_types', to='webapp.task', verbose_name='Задача')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_types', to='webapp.type', verbose_name='Тип')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_users', to='webapp.project', verbose_name='Проект')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_projects', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ManyToManyField(related_name='projects', through='webapp.ProjectUser', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='webapp.project', verbose_name='Проект'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='types',
            field=models.ManyToManyField(related_name='tasks', through='webapp.TaskType', to='webapp.Type', verbose_name='Типы'),
        ),
    ]
