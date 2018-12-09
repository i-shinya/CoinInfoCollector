from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.http import require_POST
from rest_framework import status

import requests
import json
import collections
import bson
import datetime
from pymongo import MongoClient

from externalConnect.external import ExternalConnectAdapter
from trade.models import TradeManage, UserInfo
from mymodule.myenums import TradeCode, CoinType, TradeStatus

# ビットフライヤーからマーケット情報を取得する
class GetMarketApi(APIView):
    def get(self, request, format=None):
        response = ExternalConnectAdapter.getMarkets()
        print(response.json())
        str1 = response.json()[0]
        response = ExternalConnectAdapter.getBoard()
        print(response.json())
        str = response.json()["mid_price"]
        return Response(response.json(), status=status.HTTP_200_OK)


class MongoTestApi(APIView):
    def get(self, request, format=None):
        # mongoデータベースとコレクションへ接続する
        client = MongoClient("localhost", 27017)
        db = client["test_database"]
        collection = db["test"]

        # 自身の売買情報を取得する
        trade = list(TradeManage.objects.filter(tradeStatus=TradeStatus.ORDER.name))
        orderExistFlag = False
        # 現在注文中の取引がある場合は反対売買するか判定する
        if len(trade) == 0:
            print("tradeManage is not exist")
            orderExistFlag = True

        datetime_now = datetime.datetime.now()
        date = datetime_now.date
        time = datetime_now.time

        # TODO ビットコインのボードの現在状況と価格を取得する
        response = ExternalConnectAdapter.getBoard()
        data = dict()
        data["mid_price"] = response.json()["mid_price"]
        data["date"] = str(date)
        data["time"] = str(time)
        data["bids"] = response.json()["bids"]
        data["asks"] = response.json()["asks"]
        dataList = [data]
        result = collection.insert_many(dataList)

        # TODO DBへ保存するデータを生成する to mongo

        # TODO 売買判定を行う

        # TODO 売買のリクエストを行う

        # TODO 結果をDBへ登録する

        # 例外がない場合はHTTPステータス200を返却する
        return Response(status=status.HTTP_200_OK)
