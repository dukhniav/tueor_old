import datetime

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib import admin


class Wallet(models.Model):
    class Network(models.TextChoices):
        ETHEREUM = 'ETH', _('Ethereum')
        BINANCE_SC = 'BSC', _('Binance Smart Chain')
        AVALANCHE = 'AVAX', _('Avalance')
        SOLANA = 'SOL', _('Solana')
        POLYGON = 'MATIC', _('Polygon')
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    network = Network.choices

    def __str__(self):
        return self.name

    # def was_published_recently(self):
    #     now = timezone.now()
    #     return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Transaction(models.Model):
    hash = models.CharField(max_length=200)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    interaction = models.CharField(max_length=200)
    when = models.DateTimeField

    def __str__(self):
        return self.interaction

