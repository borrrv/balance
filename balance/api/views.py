from rest_framework.views import APIView
from users.models import Users
from .serializers import UpBalanceUserSerializer
from rest_framework.generics import UpdateAPIView


class UpBalanceUserApiView(UpdateAPIView):
    """Пополнение баланса пользователя"""

    queryset = Users.objects.all()
    serializer_class = UpBalanceUserSerializer
