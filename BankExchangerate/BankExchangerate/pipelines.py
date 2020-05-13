# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# import json
#
# from scrapy.exceptions import DropItem
from ...ExchangeRate.models import GetScrapy


class GetScrapyPipeline(object):

    def process_item(self, item, spider):
        # rate = GetScrapy(bank=item.get('bank'), currency_name=item.get('currency_name'), buying_rate=item.get('buying_rate'), selling_rate=item.get('selling_rate'))
        item.save()
        print("pipeline")
        return item





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
