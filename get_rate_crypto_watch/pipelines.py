# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv
import os
import sqlalchemy as sa
import pandas as pd
import pymssql
from datetime import datetime
from config import USER_NAME, PASSWORD, IP_ADDRESS, DB_PORT, DB_NAME


class GetRateCryptoWatchPipeline(object):
    def __init__(self):
        self.filename = self.make_csv(
            ['exchange', 'currency_pair', 'currency_from', 'currency_to', 'ask_rate', 'bid_rate'])

    def make_csv(self, title):
        """
        record is a dict, choose its keys to make the first line in csv.
        :param data_type:
        :param record:
        :return:
        """
        # 今天的时间
        today_str = datetime.now().strftime('%Y-%m-%d-%H')
        today_str = today_str.replace('-', '')
        filename = 'Old\IL_CryptoWatch_Rate_' + today_str + '.csv'
        # if csv file exists, delete it
        if os.path.exists(filename):
            os.remove(filename)
        out = open(filename, 'w', newline='', encoding="utf-8")
        writer = csv.writer(out, dialect='excel')
        writer.writerow(title)
        out.close()
        return filename

    # spider开启时被调用

    def open_spider(self, spider):
        self.out = open(self.filename, 'a', newline='', encoding="utf-8")
        self.writer = csv.writer(self.out, dialect='excel')

    def process_item(self, item, spider):
        data_line = [item['exchange'], item['currency_pair'], item['currency_from'],
                     item['currency_to'], item['ask_rate'], item['bid_rate']]
        self.writer.writerow(data_line)
        return item

    def close_spider(self, spider):
        self.out.close()
        engine = sa.create_engine(
            'mssql+pymssql://{0}:{1}@{2}:{3}/{4}'.format(USER_NAME, PASSWORD, IP_ADDRESS, DB_PORT, DB_NAME))
        data = pd.read_csv(self.filename)
        data['rate_time'] = datetime.now()
        data['create_user'] = 'cryptowatch_api'
        try:
            data.to_sql('T_MST_RATE_CRYPTO_CRYPTOWATCH_JP', engine, if_exists='append', index=False, schema='dbo')
        except Exception as e:
            with open("insert_error.log", "a", encoding='utf-8') as f:
                f.write(str(datetime.now()) + ': ' + str(e))
            print('failed!')
            exit()
