#!/usr/bin/env python
import os
import sys

import logging

from mymodule.mongo_repository.dao.mongoDaoBase import MongoDaoBase

# mysqlと接続する。環境変数によって、herokuでは読み込まない。
HEROKU_FLAG = os.environ.get("DJANGO_HEROKU_FLAG", default=False)
if not HEROKU_FLAG:
    import pymysql

    pymysql.install_as_MySQLdb()

# MongoDbと接続する
MongoDaoBase.connectMongo()

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
