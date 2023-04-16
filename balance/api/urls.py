from django.urls import path, include
from .views import UpBalanceUserUpdate, ServiceViewSet, UserNewViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('service', ServiceViewSet)
router.register('users', UserNewViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include('djoser.urls')),
    path('money/<int:pk>/', UpBalanceUserUpdate.as_view()),
]
