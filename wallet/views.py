import datetime
import uuid
from uuid import UUID

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

    @action(detail=True, methods=['post'])
    def deposit(self, sender_wallet_number, amount, receiver_wallet_number):
        sender = Wallet.objects.get(pk=sender_wallet_number)
        receiver = Wallet.objects.get(pk=receiver_wallet_number)

        transaction = Transaction.objects.create()
        transaction.type = 'DEPOSIT'
        transaction.date_time = datetime.datetime.now()
        transaction.amount = amount
        transaction.wallet = sender
        transaction.reference_number = uuid.uuid4()

        updated_balance = sender.balance

        if amount > 0:
            updated_balance = sender.balance + amount

        if sender.balance != updated_balance:
            sender.balance += updated_balance
            transaction.status = 'SUCCESSFUL'
            transaction.save()
            sender.save()

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

    # @action(detail=True, methods=['post'])
    # def deposit(self, request, pk=None):
    #     wallet = self.get_object()
    # serializer =


class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
