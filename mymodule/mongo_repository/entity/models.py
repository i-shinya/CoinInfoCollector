from django.db import models
from datetime import datetime


class Test:
    def __init__(self, hoge, fuga, created=None):
        self.hoge = hoge
        self.fuga = fuga
        self.created = created or datetime.now()


class MongoModel:
    def __init__(self):
        self.coinInfoDict = dict()

    def setCommonInfo(self, coinType, date, time, datetime_str):
        self.coinInfoDict["coin_type"] = coinType.name
        self.coinInfoDict["date"] = date
        self.coinInfoDict["time"] = time
        self.coinInfoDict["datetime"] = datetime_str

    def setBoardInfo(self, response):
        self.coinInfoDict["mid_price"] = response.json()["mid_price"]
        bidList = response.json()["bids"]
        # 板データが多すぎるので1,500件に削る
        if len(bidList) > 1500:
            del bidList[1500:]
        self.coinInfoDict["bids"] = bidList
        askList = response.json()["asks"]
        if len(askList) > 1500:
            del askList[1500:]
        self.coinInfoDict["asks"] = askList

    def setTickerInfo(self, response):
        self.coinInfoDict["best_bid"] = response.json()["best_bid"]
        self.coinInfoDict["best_ask"] = response.json()["best_ask"]
        self.coinInfoDict["best_bid_size"] = response.json()["best_bid_size"]
        self.coinInfoDict["best_ask_size"] = response.json()["best_ask_size"]
        self.coinInfoDict["total_bid_depth"] = response.json()["total_bid_depth"]
        self.coinInfoDict["total_ask_depth"] = response.json()["total_ask_depth"]
        self.coinInfoDict["ltp"] = response.json()["ltp"]
        self.coinInfoDict["volume"] = response.json()["volume"]
        self.coinInfoDict["volume_by_product"] = response.json()["volume_by_product"]

