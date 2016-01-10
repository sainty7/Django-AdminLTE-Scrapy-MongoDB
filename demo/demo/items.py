# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    intern_info = scrapy.Field()
    intern_url = scrapy.Field()
    intern_company = scrapy.Field()
    intern_location = scrapy.Field()
    intern_date = scrapy.Field()
