# -*- coding: utf-8 -*-
import scrapy
from NewRealease_Amazon.items import *
from lxml import etree
import re
import urllib
import requests
from NewRealease_Amazon.settings import *
from NewRealease_Amazon.redisM import RedisM

rm = RedisM()

class amazon(scrapy.Spider):
    name = "amazonrank"
    allowed_domains = ["amazon.com"]
    
    def start_requests(self):
        global rm
        if rm.getvalue("amazonpool") == None or len(rm.getvalue("amazonpool"))<5:
            rm.pushredis("amazonpool",IPPOOL)
        start_urls = 'https://www.amazon.com/gp/new-releases/'
        yield scrapy.Request(url=start_urls, callback=self.parse,headers=AMAZON_HEADERS,meta={'cookiejar':1})
    
    def parse(self, response):
        change_proxy = False
        list = response.xpath('//ul[@id="zg_browseRoot"]/ul/li/a')  
        for one in list:
            item = NewReleaseItem()
            item['url'] = one.xpath("@href")[0].extract().strip()
            item['name'] = one.xpath("text()")[0].extract().strip()
            item['level'] =  1
            item['pname'] =  ""
            item['bigname'] = one.xpath("text()")[0].extract().strip()
            yield item
            yield scrapy.Request(url=one.xpath("@href")[0].extract().strip(),headers=AMAZON_HEADERS, callback=self.parse2, meta={'cookiejar':response.meta['cookiejar'],'change_proxy':change_proxy,'proxy':response.request.meta["proxy"]})
    
    def parse2(self, response):
        print '22222222222'
        change_proxy = False
        list = response.xpath('//ul[@id="zg_browseRoot"]/ul/ul/li/a')  
        for one in list:
            item = NewReleaseItem()
            item['url'] = one.xpath("@href")[0].extract().strip()
            item['name'] = one.xpath("text()")[0].extract().strip()
            item['level'] =  2
            item['pname'] =  response.xpath('//span[@class="zg_selected"]/text()')[0].extract().strip()
            item['bigname'] = response.xpath('//ul[@id="zg_browseRoot"]/ul/li/span/text()')[0].extract().strip()
            yield item
            yield scrapy.Request(url=one.xpath("@href")[0].extract().strip(),headers=AMAZON_HEADERS, callback=self.parse3, meta={'cookiejar':response.meta['cookiejar'],'change_proxy':change_proxy,'proxy':response.request.meta["proxy"]})
    
    def parse3(self, response):
        print '33333333333333'
        change_proxy = False
        list = response.xpath('//ul[@id="zg_browseRoot"]/ul/ul/ul/li/a')  
        for one in list:
            item = NewReleaseItem()
            item['url'] = one.xpath("@href")[0].extract().strip()
            item['name'] = one.xpath("text()")[0].extract().strip()
            item['level'] =  3
            item['pname'] =  response.xpath('//span[@class="zg_selected"]/text()')[0].extract().strip()
            item['bigname'] = response.xpath('//ul[@id="zg_browseRoot"]/ul/li/a/text()')[0].extract().strip()
            yield item
            yield scrapy.Request(url=one.xpath("@href")[0].extract().strip(),headers=AMAZON_HEADERS, callback=self.parse4, meta={'cookiejar':response.meta['cookiejar'],'change_proxy':change_proxy,'proxy':response.request.meta["proxy"]})
    
    def parse4(self, response):
        print '444444444444'
        change_proxy = False
        list = response.xpath('//ul[@id="zg_browseRoot"]/ul/ul/ul/ul/li/a')  
        for one in list:
            item = NewReleaseItem()
            item['url'] = one.xpath("@href")[0].extract().strip()
            item['name'] = one.xpath("text()")[0].extract().strip()
            item['level'] =  4
            item['pname'] =  response.xpath('//span[@class="zg_selected"]/text()')[0].extract().strip()
            item['bigname'] = response.xpath('//ul[@id="zg_browseRoot"]/ul/li/a/text()')[0].extract().strip()
            yield item
            yield scrapy.Request(url=one.xpath("@href")[0].extract().strip(),headers=AMAZON_HEADERS, callback=self.parse5, meta={'cookiejar':response.meta['cookiejar'],'change_proxy':change_proxy,'proxy':response.request.meta["proxy"]})
    
    def parse5(self, response):
        print '55555555555555'
        change_proxy = False
        list = response.xpath('//ul[@id="zg_browseRoot"]/ul/ul/ul/ul/ul/li/a')  
        for one in list:
            item = NewReleaseItem()
            item['url'] = one.xpath("@href")[0].extract().strip()
            item['name'] = one.xpath("text()")[0].extract().strip()
            item['level'] =  5
            item['pname'] =  response.xpath('//span[@class="zg_selected"]/text()')[0].extract().strip()
            item['bigname'] = response.xpath('//ul[@id="zg_browseRoot"]/ul/li/a/text()')[0].extract().strip()
            yield item
        