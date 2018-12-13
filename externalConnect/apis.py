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
from pymongo.errors import BulkWriteError

from externalConnect.external import ExternalConnector
from trade.models import TradeManage, UserInfo
from mymodule.myenums import TradeCode, CoinType, TradeStatus
from externalConnect.models import MongoModel
from mymodule.mongoRepository.mongoDaoBase import MongoDaoBase

# from mymodule.mongoRepository.tradeHistDao import TradeHistDao

# ビットフライヤーからマーケット情報を取得する
class GetMarketApi(APIView):
    def get(self, request, format=None):
        response = ExternalConnector.getMarkets()
        print(response.json())
        str1 = response.json()[0]
        response = ExternalConnector.getBoard()
        print(response.json())
        str = response.json()["mid_price"]
        return Response(response.json(), status=status.HTTP_200_OK)


class MongoTestApi(APIView):
    def get(self, request, format=None):
        # 自身の売買情報を取得する
        trade = list(TradeManage.objects.filter(tradeStatus=TradeStatus.ORDER.name))
        orderExistFlag = False  # 注文存在フラグ
        # 現在注文中の取引がある場合は反対売買するか判定する
        if len(trade) == 0:
            print("tradeManage is not exist")
            orderExistFlag = True

        datetime_now = datetime.datetime.now()
        date = datetime_now.strftime("%Y%m%d")
        time = datetime_now.strftime("%H:%M:%S")

        # ビットコインのボードの現在状況と価格を取得する
        # 例外処理をする
        try:
            coinType = CoinType.FX_BTC_JPY
            boardRes = ExternalConnector.getBoard(coinType.name)
            tickerRes = ExternalConnector.getTicker(coinType.name)

            # DBへ保存するデータを生成する to mongo
            data = MongoModel()
            data.setCommonInfo(coinType, date, time)
            data.setBoardInfo(boardRes)
            data.setTickerInfo(tickerRes)

            # DBへ保存する
            dataList = [data.coinInfoDict]
            collection = MongoDaoBase.collection
            result = collection.insert_one(data.coinInfoDict)

            # TODO 売買判定を行う

            # TODO 売買のリクエストを行う

            # TODO 結果をDBへ登録する

            # 例外がない場合はHTTPステータス200を返却する
            return Response(status=status.HTTP_200_OK)
        except RuntimeError:
            # API接続エラーの際は500エラーを返却する
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except BulkWriteError:
            # mongodb接続エラーの際は500エラーを返却する
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
