from users.models import Users
from rest_framework import serializers
from reserve.models import Service, Order, Reserve, Revenue


class CurrentUserSerializer(serializers.ModelSerializer):
    """Сериалайзер для вывода информации о пользователе"""

    order = serializers.StringRelatedField(read_only=True, many=True)

    class Meta:
        model = Users
        fields = (
            'id',
            'email',
            'balance',
            'order',
            'total',
        )


class UpBalanceUserSerializer(serializers.ModelSerializer):
    """Сериалайзер для пополнения баланса пользователя"""

    email = serializers.EmailField(required=False)

    class Meta:
        model = Users
        fields = (
            'id',
            'email',
            'balance',
        )

    """Пополнение баланса пользователя"""
    def update(self, instance, validated_data):
        balance = validated_data.get('balance')
        if instance.balance == 0:
            instance.balance = validated_data.get('balance', instance.balance)
        else:
            instance.balance += balance
        instance.save()
        return instance
    
class ServiceSerializer(serializers.ModelSerializer):
    """Сериалайзер для вывода информации об услугах"""

    class Meta:
        model = Service
        fields = (
            'id',
            'name',
            'price',
        )

class ServiceAddOrderSerializer(serializers.ModelSerializer):
    """Сериалайзер для добавление услуги в заказ"""
   
    class Meta:
        model = Order
        fields = (
            'id',
            'owner',
            'service',
            'price',
        )

    def to_representation(self, instance):
        context = {'request': self.context.get('request')}
        return ServiceSerializer(instance.service, context=context).data


class OrderForUserSerializer(serializers.ModelSerializer):
    """Сериалайзер для просмотра заказов пользователя"""

    service = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Order
        fields = (
            'id',
            'price',
            'service',
            'owner',
        )


class ReserveSerializer(serializers.ModelSerializer):
    """Сериалайзер для резервирования и просмотра средств на отдельном счете"""

    class Meta:
        model = Reserve
        fields = (
            'user',
            'reserve_balance',
        )

class RevenueSerializer(serializers.ModelSerializer):
    """Сериалайзер для признания выручки"""

    service = serializers.JSONField()
    class Meta:
        model = Revenue
        fields = (
            'user',
            'price',
            'service',
        )
