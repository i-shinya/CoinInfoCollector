from django.db import models
from datetime import datetime

# Create your models here.
class Test:
    def __init__(self, hoge, fuga, created=None):
        self.hoge = hoge
        self.fuga = fuga
        self.created = created or datetime.now()

