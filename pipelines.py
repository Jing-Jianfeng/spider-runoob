# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pdfkit
root_path=r"runoob\pdf"

class RunoobPipeline(object):
    def process_item(self, item, spider):
        url=item["url"]
        download_path=root_path+"\\"+item["title"]+".pdf"
        print(url)
        print(download_path)
        try:
            print("start download",item["title"]+".pdf")
            pdfkit.from_url(url,download_path)
        except :
            print("download",item["title"]+".pdf","wrong")

        return item
