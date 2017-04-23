# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import requests
import os
from Douban import settings
from Douban.spiders import douban_remen


class DoubanPipeline(object):
    def process_item(self, item, spider):
        # path = settings.IMAGES_STORE
        # if not os.path.exists(path):
        #     os.makedirs(path)
        # for table in item['table']:
        #     print table,'*************************************'
        #     if not os.path.exists(path+'/'+table):
        #         os.makedirs(path+'/'+table)
        path = item['path']
        # for path in path_list:

        for image_url in item['image_urls']:
            r = requests.get(image_url, verify=False)
            file_path = path+'/'+item['title'].encode('utf-8')
            # print item['title'],'******************************'
            if not os.path.exists(file_path):
                os.makedirs(file_path)
                with open(file_path+'/'+item['title'].encode('utf-8') + '.jpg', 'wb') as f:
                    for chunk in r.iter_content(chunk_size=1024):
                        if chunk:
                            f.write(chunk)
                            f.flush()
                    f.close()
            with open(file_path+'/'+item['title'].encode('utf-8') + '.txt', 'wb') as t:
                t.write(item['title'].encode('utf-8'))
                t.write(item['year'].encode('utf-8')+'\n')
                t.write('链接 :'+item['url'].encode('utf-8'))
                t.write(item['info'].encode('utf-8'))
                t.write(item['content'].encode('utf-8'))
                t.close()


        return item
