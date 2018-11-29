from django.db import models

class RawBitcoinData(models.Model):
    datetime = models.DateField()
    price_coinbase = models.FloatField()
    price_bitstamp = models.FloatField()
    volume_btc_coinbase = models.FloatField()
    volume_btc_bitstamp = models.FloatField()
    volume_currency_coinbase = models.FloatField()
    volume_currency_bitstamp = models.FloatField()
    wighted_price_coinbase = models.FloatField()
    wighted_price_bitstamp = models.FloatField()

    def __str__(self):
        return self.price_coinbase
