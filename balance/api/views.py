from users.models import Users
from .serializers import ReserveSerializer, OrderForUserSerializer, UpBalanceUserSerializer, ServiceSerializer, ServiceAddOrderSerializer, CurrentUserSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from reserve.models import Service, Order, Reserve
from djoser.views import UserViewSet
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from .permissions import IsOwner


class CustomServiceViewSet(generics.ListAPIView, viewsets.GenericViewSet,):
    pass


class UserNewViewSet(UserViewSet):
    """Работа пользователя и просмотр своих заказов"""
    queryset = Users.objects.all()
    serializer_class = CurrentUserSerializer
    pagination_class = None

    """Просмотр личных заказов пользователя"""
    @action(detail=False, methods=['get'])
    def order(self, request):
        user = request.user
        order = Order.objects.filter(owner=user)
        serializer = OrderForUserSerializer(
            instance=order,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)
    
    """Резервирование средств на отдельном счете"""
    @action(detail=True, methods=['post', 'get'])
    def reserve(self, request, id):
        user = self.request.user
        total = get_object_or_404(Users, username=user.username)
        reserve = Reserve.objects.filter(user_id=user.id)
        if request.method == 'POST':
            if total.balance >= total.total:
                if not reserve.exists():
                    total.balance -= total.total
                    total.save()
                    serializer = ReserveSerializer(
                        data={'user': user.id, 'reserve_balance': total.total}
                    )
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    return Response(serializer.data, status=HTTP_201_CREATED)
                else:
                    content = {'error': 'Данный заказ уже зарезервирован'}
                    return Response(content, status=HTTP_400_BAD_REQUEST)
            else:
                content = {'error': 'Недостаточно средств на счете'}
                return Response(content, status=HTTP_400_BAD_REQUEST)
            
        """Просмотр зарезервированных средств"""
        if request.method == 'GET':
            serializer = ReserveSerializer(reserve, many=True)
            return Response(serializer.data)

class UpBalanceUserUpdate(generics.UpdateAPIView):
    """Пополнение личного баланса пользователя"""

    queryset = Users.objects.all()
    serializer_class = UpBalanceUserSerializer
    pagination_class = None
    permission_classes = [IsOwner]


class ServiceViewSet(CustomServiceViewSet):
    """Просмотр всех услуг"""

    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    """Добавление услуги в заказ"""
    @action(detail=True, methods=['post', 'delete'])
    def add(self, request, pk=None):
        user = self.request.user
        total = get_object_or_404(Users, username=user.username)
        services = get_object_or_404(Service, pk=pk)
        obj = Order.objects.filter(owner=user, service=services)
        if self.request.method == 'POST':
            if obj.exists():
                content = {'error': 'Данная услуга уже есть в заказе'}
                return Response(content, status=HTTP_400_BAD_REQUEST)
            total.total += services.price
            total.save()
            serializer = ServiceAddOrderSerializer(
                data={'price': services.price,
                      'owner': user.id,
                      'service': services.pk,
                      },
                context={'request': self.request}
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)

        """Удаление услуги из заказа"""
        if self.request.method == 'DELETE':
            if obj.exists():
                total.total -= services.price
                total.save()
                obj.delete()
                content = {'message': 'Услуга удалена из заказа'}
                return Response(content, status=HTTP_204_NO_CONTENT)
            content={'error': 'Данной услуги нет в заказе'}
            return Response(content, status=HTTP_400_BAD_REQUEST)
