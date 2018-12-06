import json
import requests
from externalConnect.baseAdapter import BaseAdapter

rootUrl = "https://api.bitflyer.com/"

# 外部接続のアダプタークラス
# Baseアダプターを継承
class ExternalConnectAdapter(BaseAdapter):
    def getMarkets():
        path = rootUrl + "v1/getmarkets"  # 取得先のURL
        response = BaseAdapter.getRequest(path)
        return response

    def getBoard():
        path = rootUrl + "v1/getboard"
        response = BaseAdapter.getRequest(path)
        return response

    def getTicker():
        path = rootUrl + "v1/getticker"
        response = BaseAdapter.getRequest(path)
        return response
