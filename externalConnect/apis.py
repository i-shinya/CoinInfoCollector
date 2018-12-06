from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.http import require_POST
from rest_framework import status
from externalConnect.external import ExternalConnectAdapter
import requests
import json

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
