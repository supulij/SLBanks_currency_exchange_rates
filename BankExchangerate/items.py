# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


import scrapy
from scrapy_djangoitem import DjangoItem
from ExchangeRate.models import GetScrapy

print("items")


class BankexchangerateItem(DjangoItem):
    django_model = GetScrapy




# class BankexchangerateItem(scrapy.Item):
#     bank = scrapy.Field()
#     currency_name = scrapy.Field()
#     buying_rate = scrapy.Field()
#     selling_rate = scrapy.Field()


