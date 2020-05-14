from django.core.management.base import BaseCommand
from BankExchangerate.spiders.BankSpider import BankSpider1
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
# from BankExchangerate.BankExchangerate import settings as my_settings
# from scrapy.settings import Settings

print("basecommand")


class Command(BaseCommand):
    help = "Release the spiders"

    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())
        process.crawl(BankSpider1)
        process.start()

#
# crawler_settings = Settings()
# crawler_settings.setmodule(my_settings)
# process = CrawlerProcess(settings=crawler_settings)
# process.crawl(BankSpider1)
# process.start()












        # https: // github.com / Aman027 / CodeBusters