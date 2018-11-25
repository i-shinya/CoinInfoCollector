from django.urls import path
from . import apis

urlpatterns = [path("get_market/", apis.GetMarketApi.as_view(), name="extermal-test")]

