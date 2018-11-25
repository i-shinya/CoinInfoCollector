from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.http import require_POST
from rest_framework import status
import requests

# ビットフライヤーからマーケット情報を取得する
class GetMarketApi(APIView):
    def get(self, request, format=None):
        url = "https://api.bitflyer.com/v1/getmarkets"  # 取得先のURL
        response = requests.get(url)
        return Response(response.json(), status=status.HTTP_200_OK)
