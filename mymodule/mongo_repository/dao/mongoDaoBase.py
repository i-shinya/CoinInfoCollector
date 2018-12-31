from pymongo import MongoClient
from config.settings import MONGODB_INFOS

# MongoDB用のベースDao
# DBコネクションを取得し保持する。
class MongoDaoBase:
    # Mongoクライアント
    client = None
    # DBコネクション
    db = None
    # Collection
    collectionDict = None

    @classmethod
    def connectMongo(cls):
        cls.client = MongoClient(MONGODB_INFOS["HOST"], MONGODB_INFOS["PORT"])
        cls.db = cls.client[MONGODB_INFOS["NAME"]]
        cls.collection = cls.db["trade_data"] # コレクションは使用するものが追加されたらべた書きする
