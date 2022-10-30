# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AixiashuItem(scrapy.Item):
    # define the fields for your item here like:
    book_link = scrapy.Field()
    book_name = scrapy.Field()
    chapter_name = scrapy.Field()
    chapter_link = scrapy.Field()
    content = scrapy.Field()
