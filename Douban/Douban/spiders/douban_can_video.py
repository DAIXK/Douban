#coding:utf-8

import scrapy
import json
import urllib
from Douban.items import DoubanItem
from Douban import settings
import os
from scrapy.crawler import CrawlerProcess

class Douban_can_video(scrapy.Spider):
    name = 'Douban_can_video'
    item = DoubanItem()
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/j/search_subjects?']
    headers = {
        'Referer':'https://movie.douban.com/',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                       'Chrome/55.0.2883.87 Safari/537.36'
    }

    values = {
        'type': 'movie',
        'tag' : '可播放',
        'sort' : 'recommend',
        'page_limit' : '20',
        'page_start' : '0',
    }

    # 'https://movie.douban.com/j/search_subjects?'

    def start_requests(self):
        # yield scrapy.Request(self.start_urls[0],headers=self.headers,callback=self.parse)
        #热门：309  最新：500
        data = urllib.urlencode(self.values)
        url = self.start_urls[0]+data
        self.item['path'] = 'Image/可播放'
        yield scrapy.Request(url,headers=self.headers,callback=self.parse)

    def parse(self, response):
        s = json.loads(response.body)
        a = s['subjects']
        for i in xrange(len(a)):
            self.url = a[i]['url']
            self.item['url'] = self.url
            yield scrapy.Request(self.url, self.parse_info,headers=self.headers)

    def parse_info(self,response):
	print '*****************8'
        print response
        self.item['title'] = response.xpath('//h1/span[@property="v:itemreviewed"]/text()').extract()[0]
        self.item['year'] = response.xpath('//h1/span[@class="year"]/text()').extract()[0]
        self.item['image_urls'] = response.xpath('//div[@id="mainpic"][@class=""]/a/img/@src').extract()
        #处理提取多行text
        self.item['info'] = response.xpath('string(//div[@id="info"])').extract()[0]
        # content = response.xpath('string(//div[@class="related-info"])').extract()[0]
        #处理xpath提取出来打内容中的空白，只留一个
        self.item['content'] = response.xpath('normalize-space(string(//div[@class="related-info"]))').extract()[0]
        yield self.item
















