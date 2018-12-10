import json
import requests
from externalConnect.baseAdapter import BaseAdapter

rootUrl = "https://api.bitflyer.com/"

# 外部接続のアダプタークラス
# Baseアダプターを継承
class ExternalConnectAdapter(BaseAdapter):
    # マーケットの通貨情報とかを取得するメソッド（たぶん使わない）
    def getMarkets(productCode=""):
        path = rootUrl + "v1/getmarkets/"  # マーケット情報取得先のURL
        response = BaseAdapter.getRequest(path, productCode)
        return response

    # マーケットのボード情報を取得するメソッド
    def getBoard(productCode=""):
        path = rootUrl + "v1/getboardfdsafdsafds/"
        response = BaseAdapter.getRequest(path, productCode)
        return response

    # マーケットのティッカー情報を取得するメソッド
    def getTicker(productCode=""):
        path = rootUrl + "v1/getticker/"
        response = BaseAdapter.getRequest(path, productCode)
        return response
