from django.core.management.base import BaseCommand
from BankExchangerate.BankExchangerate.spiders.BankSpider import BankSpider1
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


print("basecommand")


class Command(BaseCommand):
    help = "Release the spiders"

    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())

        process.crawl(BankSpider1)
        process.start()

        # https: // github.com / Aman027 / CodeBusters