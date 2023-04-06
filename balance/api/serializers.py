from users.models import Users
from rest_framework import serializers


class CurrentUserSerializer(serializers.ModelSerializer):
    """Сериалайзер для вывода информации о пользователе"""
    class Meta:
        model = Users
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'balance',
        )


class UpBalanceUserSerializer(serializers.ModelSerializer):
    """Сериалайзер для пополнения """
    class Meta:
        model = Users
        fields = (
            'id',
            'balance',
        )

    def update(self, instance, validated_data):
        balance = validated_data.get('balance')
        if instance.balance == 0:
            instance.balance = validated_data.get('balance', instance.balance)
            instance.save()
            return instance
        else:
            instance.balance += balance
            instance.save()
            return instance
