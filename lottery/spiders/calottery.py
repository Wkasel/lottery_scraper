# -*- coding: utf-8 -*-
import scrapy
from re import sub
from decimal import Decimal


class CalotterySpider(scrapy.Spider):
    name = 'calottery'
    allowed_domains = ['calottery.com']
    start_urls = ['http://www.calottery.com/Play/Scratchers-games/$5-Scratchers/mega-crossword-1264']

    def parse(self, response):
        games = response.css('.draw_games')[0].xpath('tbody/tr')
        for g in games:
            # formatted & removed extra chars.
            prize = sub(r'[^\d.]', '', g.xpath('td/text()')[0].extract())
            odds = sub(r'[^\d.]', '', g.xpath('td/text()')[1].extract())
            winners = sub(r'[^\d.]', '', g.xpath('td/text()')[2].extract())
            claimed = sub(r'[^\d.]', '', g.xpath('td/text()')[3].extract())
            available = sub(r'[^\d.]', '', g.xpath('td/text()')[4].extract())
            checksum = int(claimed) + int(available) - int(winners) #should always equal zero
            print(prize, odds, winners, claimed, available, {'checksum':checksum})
