import scrapy
from ..items import BankexchangerateItem
from ExchangeRate.models import GetScrapy


print("bankspider1")


class BankSpider1(scrapy.Spider):
    name = 'Sampath'

    start_urls = [
            'https://www.sampath.lk/en/exchange-rates',
        ]

    def parse(self, response):
        items = BankexchangerateItem()

        items['bank'] = BankSpider1.name
        for row in response.xpath('//*[@class = "exch-rates"]/tr'):
            items['currency_name'] = row.xpath('td[1]//text()').extract_first()
            items['buying_rate'] = row.xpath('td[2]//text()').extract_first()
            items['selling_rate'] = row.xpath('td[3]//text()').extract_first()

            currency = GetScrapy()
            currency.bank = items["bank"]
            currency.currency_name = items["currency_name"]
            currency.buying_rate = items["buying_rate"]
            currency.selling_rate = items["selling_rate"]
            currency.save()

            yield items




# class BankSpider1(scrapy.Spider):
#     name = 'BOC'
#
#     start_urls = [
#             'https://www.boc.web.lk/ExRates',
#         ]
#
#     def parse(self, response):
#         items = BankexchangerateItem()
#         items['Bank'] = BankSpider1.name
#         for row in response.xpath('//tr[@class ="classTableRowColor1" or  "TableRowColor2"]'):
#             items['currency_name'] = row.xpath('td[1]/font[@class = "classFontLCNormalLabels"]//text()').extract_first()
#             items['buying_rate'] = row.xpath('td[2]//text()').extract_first()
#             items['selling_rate'] = row.xpath('td[3]//text()').extract_first()
#
#             yield items

#
# class BankSpider3(scrapy.Spider):
#     name = 'HNB'
#
#     start_urls = [
#             'https://www.hnb.net/exchange-rates',
#         ]
#
#     def parse(self, response):
#         items = BankexchangerateItem()
#         items['Bank'] = BankSpider3.name
#         for row in response.xpath('//*[@class = "table"]/tr'):
#             items['currency_name'] = row.xpath('td[1]//text()').extract_first()
#             items['buying_rate'] = row.xpath('td[3]//text()').extract_first()
#             items['selling_rate'] = row.xpath('td[4]//text()').extract_first()
#
#             yield items
#
#
# class BankSpider4(scrapy.Spider):
#     name = 'Commercial'
#
#     start_urls = [
#             'https://www.combank.net/newweb/en/rates-tariffs/exchange-rates',
#
#         ]
#
#     def parse(self, response):
#         items = BankexchangerateItem()
#         items['Bank'] = BankSpider4.name
#         for row in response.xpath('//div[@class ="rates_panel"]//tr'):
#             items['currency_name'] = row.xpath('td[1]//text()').extract_first()
#             items['buying_rate'] = row.xpath('td[2]//text()').extract_first()
#             items['selling_rate'] = row.xpath('td[3]//text()').extract_first()
#
#             yield items
#
# from django.core.management.base import BaseCommand
# from ...BankExchangerate.spiders.BankSpider import BankSpider1
# from scrapy.crawler import CrawlerProcess
# from scrapy.utils.project import get_project_settings
#
#
# class Command(BaseCommand):
#     help = "Release the spiders"
#
#     def handle(self, *args, **options):
#         process = CrawlerProcess(get_project_settings())
#
#         process.crawl(BankSpider1)
#         process.start()