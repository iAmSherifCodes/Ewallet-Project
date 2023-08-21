from rest_framework import serializers

from wallet.models import User, Wallet


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last-name', 'email', 'phone_number']


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['id', 'user', 'balance', 'wallet_number']

class CreateUserSerializer