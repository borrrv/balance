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

    class Meta:
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    price = models.PositiveIntegerField(
        verbose_name='Цена заказа',
    )
    owner = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        verbose_name='Владелец заказа',
        related_name='order',
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name='order',
        verbose_name='Услуга',
    )


    class Meta:
        verbose_name_plural = 'Заказы'
    
    def __str__(self):
        return f'{self.service} - {self.price} р.'



class Reserve(models.Model):
    user = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        related_name='reserve',
    )
    reserve_balance = models.PositiveIntegerField(
        default=0,
    )
    def __str__(self):
        return f'{self.user.username}, {self.price.price}'


class Revenue(models.Model):
    user = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        related_name='revenue'
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name='revenue',
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='revenue',
    )
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.user.username}, {self.service.name}'
    