from django.contrib.auth.models import  AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Profile(models.Model):
    avatar = models.ImageField(blank=True, null=True, upload_to='avatars', verbose_name='Аватар')
    git_link = models.URLField(blank=True, null=True, verbose_name='Ссылка на гит')
    description = models.TextField(null=True, blank=True, verbose_name='О себе')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    
    def __repr__(self):
        return self.user.get_full_name() + "'s Profile"