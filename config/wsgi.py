"""
WSGI config for django_server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from mymodule.mongo_repository.dao.mongoDaoBase import MongoDaoBase
from django.core.wsgi import get_wsgi_application

import pymysql

# Mysqlと接続する
pymysql.install_as_MySQLdb()
# MongoDbと接続する
MongoDaoBase.connectMongo()


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = get_wsgi_application()

from mymodule.scheduler import scheduler
