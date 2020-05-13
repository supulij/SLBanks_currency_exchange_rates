# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# import json
#
# from scrapy.exceptions import DropItem

from ...ExchangeRate.models import GetScrapy
import sqlite3


class GetScrapyPipeline(object):


    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("Exchangerate.db")
        self.curr = self.conn.cursor()


    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS item_tb""")
        self.curr.execute("""CREATE TABLE item_tb(
                            bank text,
                            currency_name text,
                            buying_rate text,
                            selling_rate text
                            )""")


    def process_item(self, item, spider):
        # self.store_db(item)
        # item.save()
        print("going to db")

        currency = GetScrapy()
        currency.bank = item["bank"]
        currency.currency_name = item["currency_name"]
        currency.buying_rate = item["buying_rate"]
        currency.selling_rate = item["selling_rate"]
        currency.save()
        return item

    def store_db(self, item):
        item_length = 20
        for i in range(0, item_length):
            self.curr.execute("""insert into item_tb values (?,?,?)""", (
                item['bank'][i],
                item['currency_name'][i],
                item['buying_rate'][i],
                item['selling_rate'][i]
            ))

        self.conn.commit()




# def __init__(self, unique_id, *args, **kwargs):
    #     self.unique_id = unique_id
    #     self.items = []
    #
    # @classmethod
    # def from_crawler(cls, crawler):
    #     return cls(
    #         unique_id=crawler.settings.get('unique_id'),  # this will be passed from django view
    #     )
    #
    #
    # def close_spider(self, spider):
    #     # And here we are saving our crawled data with django models.
    #     item = GetScrapy()
    #     item.unique_id = self.unique_id
    #     item.data = json.dumps(self.items)
    #     item.save()
    #
    # def process_item(self, item, spider):
    #     if 'currency_name' in item:
    #         item['currency_name'] = item['currency_name'].replace('.', '')
    #
    #     if float(item['selling_rate']) or float(item['buying_rate']) in item:
    #         pass
    #     else:
    #         raise DropItem(item)
    #
    #     return item
