import redis
#from  googleprj import settings
from datetime import datetime
from settings import *

class RedisM:
    @classmethod
    def __init__(self):
        self.r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT,password=PASSWD, decode_responses=True) 
    @classmethod
    def updateRedis(self,key,value):
        
        self.r.set(key, value)
    @classmethod
    def checkExist(self,key):
        
        lasturl = self.r.get(key)
        return lasturl
    @classmethod
    def close(self,key):
        self.r.delete(key)

    @classmethod
    def pushredis(self,key,list):
        if self.r.exists(key) == False:
            for row in list:
                self.r.rpush(key, row)
    
    @classmethod
    def popredis(self,key,otherkey):
        url = self.r.rpoplpush(key, otherkey)
        return url
    
    @classmethod
    def getvalue(self,key):
        return self.r.lrange(key, 0, -1)