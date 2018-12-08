from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.http import require_POST
from rest_framework import status

from externalConnect.external import ExternalConnectAdapter

import requests
import json
from pymongo import MongoClient

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
        # TODO 自身の売買情報を取得する

        # mongoデータベースとコレクションへ接続する
        client = MongoClient("localhost", 27017)
        db = client["test_database"]
        collection = db["test_collection"]

        # TODO ビットコインのボードの現在状況と価格を取得する
        response = ExternalConnectAdapter.getBoard()
        result = collection.insert_many(str)

        # TODO DBへ保存するデータを生成する

        # TODO 売買判定を行う

        # TODO 売買のリクエストを行う

        # TODO 結果をDBへ登録する

        # 例外がない場合はHTTPステータス200を返却する
        return Response(status=status.HTTP_200_OK)
