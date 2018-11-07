import MySQLdb
from  NewRealease_Amazon import settings
from datetime import datetime


db = MySQLdb.connect(settings.MYSQL_HOST, settings.MYSQL_USER, settings.MYSQL_PASSWORD, settings.MYSQL_DB,charset="utf8")
cursor = db.cursor()


class Sql:
    @classmethod
    def insert_category(self,item,table):
        
        pid = 0
        if item['pname'] != "":
            pidsql = "select id from "+table+" where name='"+item['pname']+"'"
            cursor.execute(pidsql)
            result = cursor.fetchone()
            if result != None:
                pid = result[0]
            print pid
        
        sql = "REPLACE  INTO "+table+" (url,name,level,bigpname,pid) VALUES ('%s', '%s', '%s', '%s', '%s')" % (item['url'],item['name'].replace("'",""),item['level'],item['bigname'].replace("'",""),pid)
        try:
            cursor.execute(sql)
            db.commit()
        except Exception,e:
            print e
            db.rollback()
    
    @classmethod
    def insert_rank(self,item,table):
        print 'sssssssssss'
        
        sql = "REPLACE  INTO "+table+" (asin,smallrank,name,bigname,title,url,price,score,reviews) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (item['asin'],item['smallrank'],item['name'],item['bigname'],item['title'].replace("'",""),item['url'],item['price'],item['score'],item['reviews'])
        try:
            cursor.execute(sql)
            db.commit()
        except Exception,e:
            print e
            db.rollback()
    