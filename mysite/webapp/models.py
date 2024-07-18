from django.db import models

# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=100, verbose_name='Тип')


    def __str__(self) -> str:
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=100, verbose_name='Статус')


    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(max_length=200, verbose_name='Описание', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата обновления')
    types = models.ManyToManyField('webapp.Type', related_name='tasks', verbose_name='Типы', through='webapp.TaskType')
    status = models.ForeignKey('webapp.Status', related_name='tasks', on_delete=models.RESTRICT, verbose_name='Статус')
    project = models.ForeignKey('webapp.Project', related_name='tasks', on_delete=models.CASCADE, verbose_name='Проект')
    is_deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
    

class TaskType(models.Model):
    task = models.ForeignKey('webapp.Task', on_delete=models.CASCADE, related_name='task_types', verbose_name='Задача')
    type = models.ForeignKey('webapp.Type', on_delete=models.CASCADE, related_name='task_types', verbose_name='Тип')

    def __str__(self) -> str:
        return f'{self.task} - {self.type}'
    

class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название проекта')
    description = models.TextField(max_length=500, verbose_name='Описание проекта')
    started_at = models.DateField(verbose_name='Дата начала') 
    ended_at = models.DateField(null=True, blank=True, verbose_name='Дата окончания')

    def __str__(self) -> str:
        return self.title

