from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ServiceViewSet, UpBalanceUserUpdate, UserNewViewSet

router = DefaultRouter()
router.register('service', ServiceViewSet)
router.register('users', UserNewViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include('djoser.urls')),
    path('money/<int:pk>/', UpBalanceUserUpdate.as_view()),
]
