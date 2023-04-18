from django.shortcuts import get_object_or_404
from djoser.views import UserViewSet
from rest_framework import generics, viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.status import (HTTP_201_CREATED, HTTP_204_NO_CONTENT,
                                   HTTP_400_BAD_REQUEST)

from reserve.models import Order, Reserve, Revenue, Service
from users.models import Users

from .permissions import IsOwner
from .serializers import (CurrentUserSerializer, OrderForUserSerializer,
                          ReserveSerializer, RevenueSerializer,
                          ServiceAddOrderSerializer, ServiceSerializer,
                          TransactionSerializer, UpBalanceUserSerializer)


class CustomServiceViewSet(generics.ListAPIView,
                           viewsets.GenericViewSet,):
    """Кастомный вьюсет для просмотра, удаления и добавления услуг в заказ"""
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
    @permission_classes([IsOwner])
    @action(detail=False, methods=['post', 'get'])
    def reserve(self, request, id=None):
        user = self.request.user
        total = get_object_or_404(Users, username=user.username)
        reserve = Reserve.objects.filter(user_id=user.id)
        orders = Order.objects.filter(owner_id=user.id)
        if request.method == 'POST':
            if total.balance >= total.total:
                if orders.exists():
                    if not reserve.exists():
                        total.balance -= total.total
                        total.save()
                        serializer = ReserveSerializer(
                            data={'user': user.id,
                                  'reserve_balance': total.total}
                        )
                        serializer.is_valid(raise_exception=True)
                        serializer.save()
                        return Response(
                            serializer.data,
                            status=HTTP_201_CREATED)
                    else:
                        content = {'error': 'Данный заказ уже зарезервирован'}
                        return Response(content, status=HTTP_400_BAD_REQUEST)
                else:
                    content = {'error': 'У вас нет активных заказов'}
                    return Response(content, status=HTTP_400_BAD_REQUEST)
            else:
                content = {'error': 'Недостаточно средств на счете'}
                return Response(content, status=HTTP_400_BAD_REQUEST)

        """Просмотр зарезервированных средств"""
        if request.method == 'GET':
            serializer = ReserveSerializer(reserve, many=True)
            return Response(serializer.data)

    """Признание выручки"""
    @action(detail=True, methods=['post'])
    def revenue(self, request, id):
        if self.request.user.is_staff:
            price = get_object_or_404(Reserve, user_id=id)
            orders = Order.objects.filter(owner_id=id)
            balance = Reserve.objects.filter(user_id=id)
            total = get_object_or_404(Users, id=id)
            balance.delete()
            serializer = RevenueSerializer(
                data={'price': price.reserve_balance,
                      'user': id,
                      'service': [o.service.name for o in orders]},
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            total.total = 0
            total.save()
            orders.delete()
            return Response(serializer.data, status=HTTP_201_CREATED)
        content = {'error': 'Признать выручку может только администратор'}
        return Response(content, status=HTTP_400_BAD_REQUEST)

    """Перевод средств другому пользователю"""
    @action(detail=True, methods=['patch'])
    def transaction(self, request, id):
        user_from = get_object_or_404(Users, id=self.request.user.id)
        user_to = get_object_or_404(Users, id=id)
        serializer = TransactionSerializer(data=request.data)
        print(serializer.initial_data['transaction'])
        print(user_from.balance)
        transaction = serializer.initial_data['transaction']
        if user_from.id == user_to.id:
            content = {'error': 'Невозможно перевести средства самому себе'}
            return Response(content, status=HTTP_400_BAD_REQUEST)
        else:
            if user_from.balance >= transaction:
                user_from.balance -= transaction
                user_from.save()
                user_to.balance += transaction
                user_to.save()
                serializer = TransactionSerializer(
                    data={'message': 'Перевод успешно совершен',
                          'balance': user_from.balance,
                          },
                )
                serializer.is_valid(raise_exception=True)
                return Response(serializer.data, status=HTTP_201_CREATED)
            else:
                content = {'error': 'На вашем счете недостаточно средств'}
                return Response(content, status=HTTP_400_BAD_REQUEST)


class UpBalanceUserUpdate(generics.UpdateAPIView):
    """Пополнение личного баланса пользователя"""

    queryset = Users.objects.all()
    serializer_class = UpBalanceUserSerializer
    pagination_class = None
    permission_classes = [IsOwner]


class ServiceViewSet(CustomServiceViewSet):
    """Просмотр, добавление и удаление услуг из заказа"""

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
            content = {'error': 'Данной услуги нет в заказе'}
            return Response(content, status=HTTP_400_BAD_REQUEST)


class RevenueListCreate(generics.ListAPIView):
    """Признание выручки и добавление средств в выручку с счета резерва"""

    queryset = Revenue.objects.all()
    serializer_class = RevenueSerializer
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):
        user = self.request.user
        price = get_object_or_404(Reserve, user_id=user.id)
        order = Order.objects.filter(owner_id=user.id)
        print(order)
        serializer = RevenueSerializer(
            data={'price': price.reserve_balance}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)
