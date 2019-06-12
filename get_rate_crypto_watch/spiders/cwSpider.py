# -*- coding: utf-8 -*-
import scrapy
import requests
import json
from get_rate_crypto_watch.items import GetRateCryptoWatchItem
from datetime import datetime
import get_rate_crypto_watch.settings


class CwspiderSpider(scrapy.Spider):
    name = 'cwSpider'
    allowed_domains = ['https://api.cryptowat.ch']
    # GET ALL VENDOR FROM API
    url = "https://api.cryptowat.ch/exchanges"
    result = requests.get(url=url).json().get('result')
    exchanges = []
    for exchange in result:
        if exchange['active']:
            exchanges.append(exchange['symbol'])
    # GET ALL CURRENCY PAIR
    with open("currency_pairs.json") as f:
        currency_pairs = json.load(fp=f).get("currency_pairs")
    urls = []
    base_url = "https://api.cryptowat.ch/markets/"
    for exchange in exchanges:
        for currency_pair in currency_pairs:
            urls.append(
                base_url + exchange + '/' + currency_pair.lower() + '/orderbook?limit=1')
    start_urls = urls

    def parse(self, response):
        item = GetRateCryptoWatchItem()
        url = response.url.split('/')
        pair = url[5].upper()
        response = response.body
        response = response.decode('utf-8')
        result = json.loads(response, strict=False).get('result')
        if result is None:
            bids = 0
            asks = 0
        elif len(result['bids']) == 0 or len(result['asks']) == 0:
            bids = 0
            asks = 0
        else:
            bids = result['bids'][0][0]  # ask rate
            asks = result['asks'][0][0]  # bid rate
        currency_from = pair[:3]
        currency_to = pair[-3:]
        if currency_from == 'DAS' or currency_from == 'ASH':
            currency_from = 'DASH'
        if currency_to == 'DAS' or currency_to == 'ASH':
            currency_to = 'DASH'
        item['exchange'] = url[4]
        item['currency_pair'] = pair
        item['currency_from'] = currency_from
        item['currency_to'] = currency_to
        item['ask_rate'] = asks
        item['bid_rate'] = bids
        yield item
