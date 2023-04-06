from rest_framework.views import APIView
from users.models import Users
from .serializers import UpBalanceUserSerializer
from rest_framework.response import Response
#from rest_framework.decorators import permission_classes
from .permissions import IsAuthor


class UpBalanceUserApiView(APIView):
    """Пополнение баланса пользователя"""
    permission_classes = [IsAuthor]

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "Метод PUT недоступен"})
        try:
            instance = Users.objects.get(pk=pk)
        except Exception:
            return Response({"error": "Объект не найден"})
        serializer = UpBalanceUserSerializer(
            data=request.data, instance=instance
            )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"result": serializer.data})
