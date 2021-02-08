import scrapy
import logging
import re
from datetime import datetime


class DailyRateSpider(scrapy.Spider):
    name = 'rate'
    start_urls = ['https://www.khanbank.com/mn/home/ratesForSites/']

    def parse(self, response):
        table = response.xpath('//table')
        rows = table.xpath('//tr')
        logging.info('ROWS:')
        logging.info(len(rows))
        for row in rows:
            tds = row.xpath('td/b/text()')
            if len(tds) == 0:
                continue
            data = {
                'date': datetime.now().strftime('%Y-%m-%d'),
                'from_currency': 'MNT',
                'to_currency': tds[0].get(),
                'buy': tds[1].get(),
                'sell': tds[2].get()
            }
            yield data
