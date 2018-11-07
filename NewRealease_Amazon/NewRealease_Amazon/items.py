# -*- coding: utf-8 -*-

import scrapy

class NewReleaseItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    level = scrapy.Field()
    pname = scrapy.Field()
    bigpid = scrapy.Field()
    bigname = scrapy.Field()
    pass

class MoversItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    level = scrapy.Field()
    bigpid = scrapy.Field()
    bigname = scrapy.Field()
    pass

class MostItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    level = scrapy.Field()
    bigpid = scrapy.Field()
    bigname = scrapy.Field()
    pass

class GiftItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    level = scrapy.Field()
    bigpid = scrapy.Field()
    bigname = scrapy.Field()
    pass

class ReleaseRankItem(scrapy.Item):
    asin = scrapy.Field()
    smallrank = scrapy.Field()
    price = scrapy.Field()
    title = scrapy.Field()
    score = scrapy.Field()
    reviews = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()
    bigname = scrapy.Field()
    pass

class MoversRankItem(scrapy.Item):
    asin = scrapy.Field()
    smallrank = scrapy.Field()
    price = scrapy.Field()
    title = scrapy.Field()
    score = scrapy.Field()
    reviews = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()
    bigname = scrapy.Field()
    pass

class MostRankItem(scrapy.Item):
    asin = scrapy.Field()
    smallrank = scrapy.Field()
    price = scrapy.Field()
    title = scrapy.Field()
    score = scrapy.Field()
    reviews = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()
    bigname = scrapy.Field()
    pass

class GiftRankItem(scrapy.Item):
    asin = scrapy.Field()
    smallrank = scrapy.Field()
    price = scrapy.Field()
    title = scrapy.Field()
    score = scrapy.Field()
    reviews = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()
    bigname = scrapy.Field()
    pass