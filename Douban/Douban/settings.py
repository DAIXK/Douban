# -*- coding: utf-8 -*-

# Scrapy settings for Douban project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'Douban'

SPIDER_MODULES = ['Douban.spiders']
NEWSPIDER_MODULE = 'Douban.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Douban (+http://www.yourdomain.com)'
# ITEM_PIPELINES = {'scrapy.contrib.pipeline.images.ImagesPipeline': 1}

ITEM_PIPELINES = {'Douban.pipelines.DoubanPipeline':300}
# IMAGES_STORE = ''

ROBOTSTXT_OBEY = True
