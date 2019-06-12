# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GetRateCryptoWatchItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    exchange = scrapy.Field()
    currency_pair = scrapy.Field()
    currency_from = scrapy.Field()
    currency_to = scrapy.Field()
    ask_rate = scrapy.Field()
    bid_rate = scrapy.Field()
