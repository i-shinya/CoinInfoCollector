import requests
from rest_framework.response import Response

# 外部接続の基底クラス
# 共通メソッドとエラーハンドリングを定義する
class BaseAdapter:
    def getRequest(path):
        respose = requests.get(path)
        return respose

