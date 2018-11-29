from django.db import models

class RawBitcoinData(models.Model):
    datetime = models.DateField(primary_key=True)
    price_coinbase = models.FloatField(null=True)
    price_bitstamp = models.FloatField(null=True)
    volume_btc_coinbase = models.FloatField(null=True)
    volume_btc_bitstamp = models.FloatField(null=True)
    volume_currency_coinbase = models.FloatField(null=True)
    volume_currency_bitstamp = models.FloatField(null=True)
    wighted_price_coinbase = models.FloatField(null=True)
    wighted_price_bitstamp = models.FloatField(null=True)

    def __str__(self):
        return self.price_coinbase
