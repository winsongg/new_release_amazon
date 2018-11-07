# -*- coding: utf-8 -*-

import json
from .sql import Sql
import settings
from items import *


class Pipeline(object):

    def process_item(self, item, spider):
        if isinstance(item,NewReleaseItem):
            Sql.insert_category(item,"release_category")
        if isinstance(item,MoversItem):
            Sql.insert_category(item,"most_category")
        if isinstance(item,MostItem):
            Sql.insert_category(item,"gift_category")
        if isinstance(item,GiftItem):
            Sql.insert_category(item,"movers_category")
        
        if isinstance(item,ReleaseRankItem):
            Sql.insert_rank(item,"release_rank")
        if isinstance(item,MoversRankItem):
            Sql.insert_rank(item,"most_rank")
        if isinstance(item,MostRankItem):
            Sql.insert_rank(item,"gift_rank")
        if isinstance(item,GiftRankItem):
            Sql.insert_rank(item,"movers_rank")
        return item
    