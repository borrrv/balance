from django.urls import path, include
from .views import UpBalanceUserUpdate, ServiceViewSet, UserNewViewSet#, RevenueListCreate
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('service', ServiceViewSet)
router.register('users', UserNewViewSet)
#router.register('revenue', RevenueListCreate)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include('djoser.urls')),
    path('money/<int:pk>/', UpBalanceUserUpdate.as_view()),
    #path('revenue/', RevenueListCreate.as_view()),
]
