from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from wallet.models import User, Wallet, Transaction
from wallet.serializers import UserSerializer, WalletSerializer, TransactionSerializer


# Create your views here.
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# DEPOSIT
#

class WalletViewSet(ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

    # @action(detail=True, methods=['post'])
    # def set_password(self, request, pk=None):
    #     user = self.get_object()
    #     serializer = PasswordSerializer(data=request.data)
    #     if serializer.is_valid():
    #         user.set_password(serializer.validated_data['password'])
    #         user.save()
    #         return Response({'status': 'password set'})
    #     else:
    #         return Response(serializer.errors,
    #                         status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def deposit(self, request, pk=None):
        wallet = self.get_object()
        # serializer =


class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
