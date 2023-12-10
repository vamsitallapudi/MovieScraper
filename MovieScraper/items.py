# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MoviescraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class BookmyshowScraperItem(scrapy.Item):
    title = scrapy.Field()


class PaytmScraperItem(scrapy.Item):
    title = scrapy.Field()


class AmazonScraperItem(scrapy.Item):
    product_title = scrapy.Field()
