from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from wallet.models import Wallet


# WHEN A USER IS CREATED THIS METHOD IS INVOKED
@receiver(post_save, sender=Wallet)
def create_wallet(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(user=instance, wallet_number=instance.phone[1:])
