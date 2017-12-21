# -*- coding: utf-8 -*-
import scrapy


class CalotterySpider(scrapy.Spider):
    name = 'calottery'
    allowed_domains = ['calottery.com']
    start_urls = ['http://www.calottery.com/Play/Scratchers-games/$5-Scratchers/mega-crossword-1264']

    def parse(self, response):
        games = response.css('.draw_games')[0].xpath('tbody/tr')
        for g in games:
            prize = g.xpath('td/text()')[0].extract()
            odds = g.xpath('td/text()')[1].extract()
            winners = g.xpath('td/text()')[2].extract()
            claimed = g.xpath('td/text()')[3].extract()
            available = g.xpath('td/text()')[4].extract()
            print(prize, odds, winners, claimed, available)
