# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo 
import time
from datetime import * 
from scrapy.conf import settings

class MongoDBPipeline(object):
    def __init__(self):
	date1 = str(date.today()).replace('-','')
        coll1_name = settings['MONGODB_COLLECTION']+date1
	client = pymongo.MongoClient(settings['MONGODB_URI'],settings['MONGODB_PORT'])
	db = client[settings['MONGODB_DB']]
	self.coll1 = db[coll1_name]
	coll2_name = coll1_name[:-2]+str(int(coll1_name[-2:])-2)
	self.coll2 = db[coll2_name]
	if self.coll1.count() != 0:
		self.coll1.remove()
	if self.coll2.count() != 0:
		self.coll2.remove()
    def process_item(self, item, spider):
	self.coll1.insert(dict(item))
        return item








