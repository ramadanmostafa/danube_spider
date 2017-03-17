# -*- coding: utf-8 -*-
import scrapy
from ..items import DanubeSpiderItem


class DanubeSpider(scrapy.Spider):
    name = "danube"
    allowed_domains = ["danube.sa"]
    start_urls = (
        'http://www.danube.sa/',
    )

    def parse(self, response):
        """
        get a list of all categories available and yield a request for every page
        """
        categories_urls_xpath = '//*[@id="cate-list"]/dl/dt/a/@href'
        categories_urls = response.xpath(categories_urls_xpath).extract()

        for url in categories_urls:
            yield scrapy.Request(response.urljoin(url), self.parse_category)

    def parse_category(self, response):
        """
        get a list of item details pages and yield a request for every page
        it also calls itself for the next pages if exists
        """
        item_urls_xpath = '//*[@id="catalog-listing"]/div[3]/div/div/div[2]/a/@href'
        next_pages_xpath = '//*[@id="catalog-listing"]/div[2]/div[2]/ol/li/a/@href'
        item_urls = response.xpath(item_urls_xpath).extract()
        for url in item_urls:
            yield scrapy.Request(response.urljoin(url), self.parse_item)

        next_pages = response.xpath(next_pages_xpath).extract()
        for url in next_pages:
            yield scrapy.Request(response.urljoin(url), self.parse_category)

    def parse_item(self, response):
        """
        parse the item details page and download the images
        """
        name_arabic_xpath = '//*[@id="product_addtocart_form"]/div[3]/div[2]/span/text()'
        price_xpath = '//span[@class="price"]/text()'
        item_details_xpath = '//div[@class="product-collateral"]/p/text()'
        image_urls_xpath = '//*[@id="product_addtocart_form"]/div[2]/div[2]/div/img/@src'

        item = DanubeSpiderItem()
        item['item_page_url'] = response.url
        item['name_english'] = response.url.split('/')[-1].split('.')[0]
        item['name_arabic'] = response.xpath(name_arabic_xpath).extract_first()
        item['price'] = response.xpath(price_xpath).extract_first()
        #download images
        item['image_urls'] = response.xpath(image_urls_xpath).extract()

        item_details = response.xpath(item_details_xpath).extract()
        num_details = len(item_details)

        item['description'] = ''
        item['barcode'] = ''
        item['weight'] = ''

        if num_details == 1:
            item['description'] = item_details[0]

        elif num_details == 2:
            item['description'] = item_details[0]
            item['barcode'] = item_details[1]

        elif num_details >= 3:
            item['description'] = item_details[0]
            item['barcode'] = item_details[-2]
            item['weight'] = item_details[-1]

        yield item
