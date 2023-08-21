from rest_framework.viewsets import ModelViewSet

from wallet.models import User, Wallet, Transaction
from wallet.serializers import UserSerializer, WalletSerializer, TransactionSerializer


# Create your views here.
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class WalletViewSet(ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
