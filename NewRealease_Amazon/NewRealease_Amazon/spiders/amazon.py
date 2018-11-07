# -*- coding: utf-8 -*-
import scrapy
from NewRealease_Amazon.items import *
from lxml import etree
import re
import urllib
import requests
from NewRealease_Amazon.settings import *
from NewRealease_Amazon.redisM import RedisM
import MySQLdb

rm = RedisM()
db = MySQLdb.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB,charset="utf8")
cursor = db.cursor()

class amazon(scrapy.Spider):
    name = "release"
    allowed_domains = ["amazon.com"]
    
    def start_requests(self):

        #填充要爬的排名url
        sql = "select bigpname,name,url from release_category"
        cursor.execute(sql)
        keywords = cursor.fetchall()
        for row in keywords:
            #填充IP池
            if rm.getvalue("amazonpool") == None or len(rm.getvalue("amazonpool"))<5:
                rm.pushredis("amazonpool",IPPOOL)
            key = row
            print key
            yield scrapy.Request(url=key[2], callback=self.parse,headers=AMAZON_HEADERS,meta={'cookiejar':1,'bigname':key[0],'name':key[1]})
            rm.close(key)
        
    def parse(self, response):
        print '11111111'
        change_proxy = False
        list = response.xpath('//*[@id="zg-ordered-list"]/li') 
        
        for one in list:
            item = ReleaseRankItem()
            if len(one.xpath('span/div/span/a/@href'))>0:
                item['url'] = "https://www.amazon.com"+one.xpath('span/div/span/a/@href')[0].extract()
            else:
                item['url'] = ""
            item['name'] = response.request.meta['name']
            if len(one.xpath('span/div/span/a'))>0:
                tempasin = one.xpath('span/div/span/a')[0].extract()
                item['asin'] = tempasin[tempasin.index('dp/')+3:tempasin.index('/ref')]
            else:
                item['asin'] = ""
            if len(one.xpath('span/div/span/a/div/text()'))>0:
                item['title'] = one.xpath('span/div/span/a/div/text()')[0].extract().replace("'","").strip()
            else:
                item['title'] = ''
            
            if len(one.xpath('span/div/span/div[1]/a[1]/i/span/text()'))>0:
                tempscore = one.xpath('span/div/span/div[1]/a[1]/i/span/text()')[0].extract()
                item['score'] = tempscore[0:tempscore.index(' out')]
            else:
                item['score'] = '0'
            if len(one.xpath('span/div/span/div[1]/a[2]/text()'))>0:
                item['reviews'] = one.xpath('span/div/span/div[1]/a[2]/text()')[0].extract()
            else:
                item['reviews'] = '0'
            if len(one.xpath('span/div/span/div[2]/a/span/span/text()'))>0:
                item['price'] = one.xpath('span/div/span/div[2]/a/span/span/text()')[0].extract()
            else:
                item['price'] = '0'
            
            item['smallrank'] = one.xpath("span/div/div/span[1]/span/text()")[0].extract().strip().replace("#","")
            
            item['bigname'] = response.request.meta['bigname']
            yield item
        
        #有下一页就继续跳转
        if len(response.xpath('//*[@class="a-last"]/a')) > 0 :
            print 'next page'
            yield scrapy.Request(url=response.xpath('//*[@class="a-last"]/a/@href')[0].extract(),headers=AMAZON_HEADERS, callback=self.parse, meta={'cookiejar':response.meta['cookiejar'],'change_proxy':change_proxy,'proxy':response.request.meta["proxy"],'bigname':response.request.meta["bigname"],'name':response.request.meta["name"]})
    
    