# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# import json
import re
from scrapy.exceptions import DropItem
from ExchangeRate.models import GetScrapy
import sqlite3

import datetime

def curreny_process(item):
    if float(item['selling_rate']) or float(item['buying_rate']) in item:
        pass
    else:
        raise DropItem(item)

    if 'currency_name' in item:
        item['currency_name'] = item['currency_name'].replace('.', '')
        item['currency_name'] = re.sub(" \(.*?\)" , "", item['currency_name'])

    result = re.search("(Dollars|Kroner|Dinars|Francs|Riyals|Dirhams)$", item['currency_name'])
    if result:
        item['currency_name'] = re.sub(".$","", item['currency_name'])

    if item['currency_name'] in ['British Pounds','Great Britain Pounds','Great Britain Pound','Pounds Sterling']:
        item['currency_name'] = 'UK Pound'
    elif item['currency_name'] == 'Chinese Renminbi':
        item['currency_name'] = 'Chinese Yuan'
    elif item['currency_name'] == 'Omanian Riyal':
        item['currency_name'] = 'Omani Riyal'
    elif item['currency_name'] == 'EURO':
        item['currency_name'] = 'Euro'
    elif item['currency_name'] == 'Hongkong Dollar':
        item['currency_name'] = 'Hong Kong Dollar'
    elif item['currency_name'] == 'Norweigian Krone':
        item['currency_name'] = 'Norwegian Krone'
    elif item['currency_name'] in ['UAE Dirams', 'United Arab Emirates Dirham']:
        item['currency_name'] = 'UAE Dirham'
    elif item['currency_name'] == 'Swedish Krone':
        item['currency_name'] = 'Swedish Krona'

    return item


class BankexchangerateItemPipeline(object):

    def process_item(self, item, spider):

        item = curreny_process(item)
        item['updated'] = datetime.datetime.now()

        item['id'] = item['bank'] + item['currency_name']
        currency = GetScrapy()

        currency.bank = item["bank"]
        currency.currency_name = item["currency_name"]
        currency.buying_rate = item["buying_rate"]
        currency.selling_rate = item["selling_rate"]
        currency.id = item['id']
        currency.updated = item['updated']

        currency.save()
        return item







    # def __init__(self):
    #     self.create_connection()
    #     self.create_table()
    #
    # def create_connection(self):
    #     self.conn = sqlite3.connect("Exchangerate.db")
    #     self.curr = self.conn.cursor()
    #
    # def create_table(self):
    #     self.curr.execute("""DROP TABLE IF EXISTS item_tb""")
    #     self.curr.execute("""CREATE TABLE item_tb(
    #                         bank text,
    #                         currency_name text,
    #                         buying_rate text,
    #                         selling_rate text
    #                         )""")

    # if 'currency_name' in item:
    #     item['currency_name'] = item['currency_name'].replace('.', '')
    # if float(item['selling_rate']) or float(item['buying_rate']) in item:
    #     pass
    # else:
    #     raise DropItem(item)

    # self.store_db(item)

    # def store_db(self, item):
    #     # print("storing")
    #     self.curr.execute("""insert into item_tb values (?,?,?,?)""", (
    #             item['bank'],
    #             item['currency_name'],
    #             item['buying_rate'],
    #             item['selling_rate']
    #         ))
    #
    #     self.conn.commit()

#
# class CurrencyprocessPipeline(object):
#     print('process items')
#
#     def process_item(self, item, spider):
#         if 'currency_name' in item:
#             item['currency_name'] = item['currency_name'].replace('.', '')
#
#         if float(item['selling_rate']) or float(item['buying_rate']) in item:
#             pass
#         else:
#             raise DropItem(item)
#         item.save()
#         yield item