import requests
from rest_framework.response import Response

# 外部接続の基底クラス
# 共通メソッドとエラーハンドリングを定義する
class BaseAdapter:
    def getRequest(path, productCode):
        if productCode != "":
            param = "?product_code=" + productCode
            path = path + param
        respose = requests.get(path)
        if respose.status_code != 200:
            raise RuntimeError("failed to connect bit-flyer_api")
        return respose

