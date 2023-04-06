from django.urls import path, include
from .views import UpBalanceUserApiView



urlpatterns = [
    path('auth/', include('djoser.urls.authtoken')),
    path('', include('djoser.urls')),
    path('money/<int:pk>/', UpBalanceUserApiView.as_view()),
]
