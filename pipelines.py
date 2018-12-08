# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient


class MusicScrapyPipeline(object):
    def __init__(self):
        uname = 'root'
        passwd = '123456'
        host = '10.0.217.234'
        port = 27017
        the_db = 'songs'
        mc = MongoClient(host, port)
        db = mc[the_db]
        # db.authenticate(uname, passwd)
        self._db = db

    def process_item(self, item, spider):
        print('*'*100)
        print(item)

        if not self._db['album_task'].find_one({'url': item['url']}):
            self._db['album_task'].insert_one(item)

        return item
