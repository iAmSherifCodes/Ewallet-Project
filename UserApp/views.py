from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from wallet.models import User
from wallet.serializers import UserSerializer


# Create your views here.

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
