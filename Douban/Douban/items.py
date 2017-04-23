# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    title = scrapy.Field()
    year = scrapy.Field()
    image_urls = scrapy.Field()
    info = scrapy.Field()
    content = scrapy.Field()
    path = scrapy.Field()


