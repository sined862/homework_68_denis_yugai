from django.db import models
from django.contrib.auth.models import AbstractUser

class Account(AbstractUser):
    email = models.EmailField(
        max_length=20,
        verbose_name='Электронная почта', 
        null=False,
        blank=False
    )
    phone = models.CharField(
        max_length=10,
        verbose_name='Номер телефона',
        null=False,
        blank=False
    )
    telegram = models.CharField(
        max_length=30,
        verbose_name='Telegram',
        null=False,
        blank=False
    )
    facebook = models.CharField(
        max_length=30,
        verbose_name='Facebook',
        null=True,
        blank=True
    )
    linkedin = models.CharField(
        max_length=30,
        verbose_name='Linkedin',
        null=True,
        blank=True
    )
    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to='avatars',
        verbose_name='Аватар'
    )
    is_employer = models.BooleanField(
        verbose_name='Работодатель:',
        null=False,
        blank=False
    )

    def __str__(self):
        return self.username

    