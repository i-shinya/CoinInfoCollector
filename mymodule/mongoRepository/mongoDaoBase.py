from pymongo import MongoClient

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
        cls.client = MongoClient("localhost", 27017)
        cls.db = cls.client["test_database"]
        cls.collection = cls.db["trade"]
