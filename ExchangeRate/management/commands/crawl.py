from django.core.management.base import BaseCommand
from BankExchangerate.spiders.BankSpider import BankSpider1, BankSpider2, BankSpider3, BankSpider4
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# print("basecommand")


class Command(BaseCommand):
    help = "Release the spiders"

    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())
        process.crawl(BankSpider1)
        process.crawl(BankSpider2)
        process.crawl(BankSpider3)
        process.crawl(BankSpider4)
        process.start()
