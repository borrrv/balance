from django.db import models
from users.models import Users


class Service(models.Model):
    name = models.CharField(
        max_length=150,
        blank=False,
        unique=True,
        verbose_name='Наименование услуги'
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена услуги'
    )


class Order(models.Model):
    price = models.PositiveIntegerField(
        verbose_name='Цена заказа',
    )
    owner = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        verbose_name='Заказ пользователя',
        related_name='order',
    )


class ServiceUser(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        verbose_name='Наименование услуги',
        related_name='services',
    )
    users = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        verbose_name='Пользователь с услугой',
        related_name='services',
    )


class OrderUsers(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name='Заказ пользователя',
        related_name='orders',
    )
    users = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='orders',
    )
