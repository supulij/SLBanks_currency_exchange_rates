import scrapy
from BankExchangerate.items import BankexchangerateItem

# print("bankspider1")


class BankSpider1(scrapy.Spider):
    name = 'Sampath'

    start_urls = [
            'https://www.sampath.lk/en/exchange-rates',
        ]

    def parse(self, response):
        item = BankexchangerateItem()

        item['bank'] = BankSpider1.name
        for row in response.xpath('//*[@class = "exch-rates"]/tr'):
            item['currency_name'] = row.xpath('td[1]//text()').extract_first()
            item['buying_rate'] = row.xpath('td[2]//text()').extract_first()
            item['selling_rate'] = row.xpath('td[3]//text()').extract_first()
            # item['id'] = item['bank']+item['currency_name']

            yield item


class BankSpider2(scrapy.Spider):
    name = 'BOC'

    start_urls = [
            'https://www.boc.web.lk/ExRates',
        ]

    def parse(self, response):
        item = BankexchangerateItem()
        item['bank'] = BankSpider2.name
        for row in response.xpath('//tr[@class ="classTableRowColor1" or  "TableRowColor2"]'):
            item['currency_name'] = row.xpath('td[1]/font[@class = "classFontLCNormalLabels"]//text()').extract_first()
            item['buying_rate'] = row.xpath('td[2]//text()').extract_first()
            item['selling_rate'] = row.xpath('td[3]//text()').extract_first()
            # item['id'] = item['bank'] + item['currency_name']

            yield item


class BankSpider3(scrapy.Spider):
    name = 'HNB'

    start_urls = [
            'https://www.hnb.net/exchange-rates',
        ]

    def parse(self, response):
        item = BankexchangerateItem()
        item['bank'] = BankSpider3.name
        for row in response.xpath('//*[@class = "table"]/tr'):
            item['currency_name'] = row.xpath('td[1]//text()').extract_first()
            item['buying_rate'] = row.xpath('td[3]//text()').extract_first()
            item['selling_rate'] = row.xpath('td[4]//text()').extract_first()
            # item['id'] = item['bank'] + item['currency_name']

            yield item


class BankSpider4(scrapy.Spider):
    name = 'Commercial'

    start_urls = [
            'https://www.combank.net/newweb/en/rates-tariffs/exchange-rates',

        ]

    def parse(self, response):
        item = BankexchangerateItem()
        item['bank'] = BankSpider4.name
        for row in response.xpath('//div[@class ="rates_panel"]//tr'):
            item['currency_name'] = row.xpath('td[1]//text()').extract_first()
            item['buying_rate'] = row.xpath('td[2]//text()').extract_first()
            item['selling_rate'] = row.xpath('td[3]//text()').extract_first()
            # item['id'] = item['bank'] + item['currency_name']

            yield item


class BankSpider5(scrapy.Spider):
    name = "People's Bank"

    start_urls = [
            'https://www.peoplesbank.lk/foreign-exchange-rates',

        ]

    def parse(self, response):
        items = BankexchangerateItem()
        items['bank'] = BankSpider5.name
        for row in response.xpath('//div[@class ="table-responsive rates-table"]//tr'):
            items['currency_name'] = row.xpath('td[2]//text()').extract_first()
            items['buying_rate'] = row.xpath('td[3]//text()').extract_first()
            items['selling_rate'] = row.xpath('td[4]//text()').extract_first()

            yield items


class BankSpider6(scrapy.Spider):
    name = 'Seylan'

    start_urls = [
            'https://www.seylan.lk/exchange-rates',

        ]

    def parse(self, response):
        items = BankexchangerateItem()
        items['bank'] = BankSpider6.name
        for row in response.xpath('//div[@class ="container xrate_container table-responsive"]//tr'):
            items['currency_name'] = row.xpath('td[2]//text()').extract_first()
            items['buying_rate'] = row.xpath('td[4]//text()').extract_first()
            items['selling_rate'] = row.xpath('td[5]//text()').extract_first()

            yield items


