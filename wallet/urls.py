from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter
router.register('users', views.UserViewSet, basename="users")
# router.register('wallets', views.)

urlpatterns = [
    path('/user', views.UserViewSet),
    path('/transactions', views.TransactionViewSet),
    path('/wallet', views.WalletViewSet)
]
