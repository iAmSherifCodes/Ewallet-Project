import uuid

from django.db import models


# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email}"


class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    balance = models.BigIntegerField()
    wallet_number = models.CharField(max_length=10, primary_key=True)


class Transaction(models.Model):
    TYPES = [
        ('NONE', 'None'),
        ('TRANSFER', 'Transfer'),
        ('DEPOSIT', 'Deposit'),
    ]

    STATUS_TYPES = [
        ('PENDING', 'Pending'),
        ('SUCCESSFUL', 'Successful'),
        ('REJECTED', 'Rejected')
    ]

    type = models.CharField(max_length=8, choices=TYPES, default="None")
    status = models.CharField(max_length=10, choices=STATUS_TYPES, default="Pending")
    date_time = models.DateTimeField(auto_now_add=True)
    amount = models.BigIntegerField()
    wallet = models.ForeignKey(Wallet, on_delete=models.PROTECT)
    reference_number = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
