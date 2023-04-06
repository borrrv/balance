from users.models import Users
from rest_framework import serializers


class CurrentUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'balance',
        )
