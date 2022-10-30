import re

import scrapy
from aixiashu.items import AixiashuItem

class NovelSpider(scrapy.Spider):
    name = 'novel'
    allowed_domains = ['aixiaxsw.com']
    start_urls = ['https://www.aixiaxsw.com/?ref=dartools.com']

    def parse(self, response):

        book_link_list=response.xpath('//*[@class="novelslist"]/div/ul/li/a/@href | //*[@class="novelslist"]/div/div/dl/dt/a/@href').extract()
        # print(len(book_link_list))
        for book_link in book_link_list[:1]:
            yield scrapy.Request(
                url=book_link,
                callback=self.parse_chapter,
                meta={'book_link':book_link}
            )
    def parse_chapter(self,response):
        temp={}
        temp['book_link']=response.meta['book_link']
        temp['book_name']=response.xpath('//*[@id="info"]/h1/text()').extract_first()
        # print(book_name,book_link)
        chapter_list=response.xpath('//*[@id="list"]/dl/dd')

        for chapter in chapter_list[:1]:
            temp['chapter_name'] = chapter.xpath('./a/text()').extract_first()
            temp['chapter_link'] = response.urljoin(chapter.xpath('./a/@href').extract_first())
            yield scrapy.Request(
                url=temp['chapter_link'],
                callback=self.parse_content,
                meta={'book':temp}
            )
    def parse_content(self,response):
        book=AixiashuItem()
        temp=response.meta['book']
        book['book_link']=temp['book_link']
        book['book_name']=temp['book_name']
        book['chapter_name']=temp['chapter_name']
        book['chapter_link']=temp['chapter_link']
        book['content']=str(response.xpath('//*[@id="content"]/text()').extract()).strip()
        # pat='&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br><br>'
        # print(response.body.decode())
        # book['content'] = re.compile(pat).findall(response.body.decode())

        # book['content']=book['content'].split('\xa0\xa0\xa0\xa0')[1].split(", '\n', '\n")[0]
        # print(book['content'])
        yield book

