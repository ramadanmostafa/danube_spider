# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DanubeSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    item_page_url = scrapy.Field()
    name_english = scrapy.Field()
    name_arabic = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()
    barcode = scrapy.Field()
    weight = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
