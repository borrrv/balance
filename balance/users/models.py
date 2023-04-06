from django.db import models
from django.contrib.auth.models import AbstractUser
from balance.settings import MAX_LENGTH


class Users(AbstractUser):
    email = models.EmailField(
        blank=False,
        unique=True,
        help_text='Введите вашу почту'
    )
    first_name = models.CharField(
        blank=False,
        help_text='Введите ваше имя',
        max_length=MAX_LENGTH,
    )
    last_name = models.CharField(
        blank=False,
        help_text='Введите вашу фамилию',
        max_length=MAX_LENGTH,
    )
    balance = models.PositiveIntegerField(
        help_text='Баланс пользователя',
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'