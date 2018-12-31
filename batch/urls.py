from django.urls import path
from . import apis

urlpatterns = [
    path("get_market/", apis.GetMarketApi.as_view(), name="extermal-test"),
    path("test_api/", apis.TestApi.as_view(), name="test"),
    path("auto_trade/", apis.AutoTradeApi.as_view(), name="auto-trade"),
]
