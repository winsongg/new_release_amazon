# -*- coding: utf-8 -*-
import random  
from scrapy import signals  
from NewRealease_Amazon.settings import *
import requests
from NewRealease_Amazon.redisM import RedisM

rm = RedisM()
  
class ProxyMiddleware1(object):  
  
    def __init__(self,ip=''):  
          self.ip=ip  
        
    def process_request(self, request, spider): 
        # spider发现parse error, 更换代理

        if "proxy" not in request.meta.keys() or ("change_proxy" in request.meta.keys() and request.meta["change_proxy"]):
            thisip = ""
            if "google.com" in request.url:
                dict = eval(rm.popredis("googlepool","google_dealpool"))
                thisip = dict
            elif "baidu.com" in request.url:
                dict = eval(rm.popredis("baidupool","baidu_dealpool"))
                thisip = dict
            elif "amazon.com" in request.url:
                dict = eval(rm.popredis("amazonpool","amazon_dealpool"))
                thisip = dict
                
            print "thisip:"+thisip["ipaddr"]
            request.meta["change_proxy"] = False
            request.meta["proxy"]="http://"+thisip["ipaddr"]  
        
        
    def process_response(self, request, response, spider):

        statuslist = [503,502,500,403,302,303]
        if response.status in statuslist:
            thisip = ""
            if "google.com" in request.url:
                dict = eval(rm.popredis("googlepool","google_dealpool"))
                thisip = dict
            elif "baidu.com" in request.url:
                dict = eval(rm.popredis("baidupool","baidu_dealpool"))
                thisip = dict
            elif "amazon.com" in request.url:
                dict = eval(rm.popredis("amazonpool","amazon_dealpool"))
                thisip = dict
            print "状态码错误，需要更换IP:"+str(response.status)
            request.meta["change_proxy"] = False
            request.meta["proxy"]="http://"+thisip["ipaddr"]  
            new_request = request.copy()
            new_request.dont_filter = True
            return new_request
        else:
            return response