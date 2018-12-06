import requests
from rest_framework.response import Response


class BaseAdapter:
    def getRequest(path):
        respose = requests.get(path)
        return respose

