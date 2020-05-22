from django.core.management.base import BaseCommand
from BankExchangerate.spiders.BankSpider import BankSpider1, BankSpider2, BankSpider3, BankSpider4, BankSpider5, BankSpider6


from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging


# print("basecommand")


class Command(BaseCommand):
    help = "Release the spiders"

    def handle(self, *args, **options):
        configure_logging()
        runner = CrawlerRunner()
        runner.crawl(BankSpider1)
        runner.crawl(BankSpider2)
        runner.crawl(BankSpider3)
        runner.crawl(BankSpider4)
        runner.crawl(BankSpider5)
        runner.crawl(BankSpider6)
        d = runner.join()
        d.addBoth(lambda _: reactor.stop())

        reactor.run()  # the script will block here until all crawling jobs are finished
