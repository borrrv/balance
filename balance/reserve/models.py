from django.db import models

from users.models import Users


class Service(models.Model):
    """Модель услуг"""
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
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'price'],
                name='unique_name_price'
            )
        ]

    def __str__(self):
        return f'{self.name} - {self.price}'


class Order(models.Model):
    """Модель заказов"""
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
        return f'{self.service.name} - {self.price} р.'


class Reserve(models.Model):
    """Модель счета для резерва средств"""
    user = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        related_name='reserve',
    )
    reserve_balance = models.PositiveIntegerField(
        default=0,
    )

    def __str__(self):
        return f'{self.user.username}, {self.reserve_balance}'


class Revenue(models.Model):
    """Модель выручки"""
    user = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        related_name='revenue'
    )
    price = models.PositiveIntegerField()
    service = models.CharField(
        max_length=150,
    )

    def __str__(self):
        return f'{self.user.username}, {self.service.name}'
