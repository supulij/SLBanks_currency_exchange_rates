from django.db import models
# import json


class GetScrapy(models.Model):
    bank = models.CharField(max_length=25)
    currency_name = models.CharField(max_length=50)
    id = models.CharField(max_length=100, primary_key=True)
    buying_rate = models.CharField(max_length=20)
    selling_rate = models.CharField(max_length=20)

    class Meta:
        db_table = 'Exchange_Rates'
        ordering = ['currency_name']

    def __str__(self):
        return '{} {}'.format(self.bank, self.currency_name)


  # @property
    # def to_dict(self):
    #     data = {
    #         'bank': json.loads(self.bank),
    #         'currency_name': json.loads(self.currency_name),
    #         'buying_rate': json.loads(self.buying_rate),
    #         'selling_rate': json.loads(self.selling_rate),
    #
    #     }
    #     return data