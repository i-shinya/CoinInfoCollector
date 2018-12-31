from django.urls import path
from . import apis

urlpatterns = [
    path("get_market/", apis.GetMarketApi.as_view(), name="extermal-test"),
    path("auto_trade/", apis.AutoTradeApi.as_view(), name="auto-trade"),
]

# 以下でbatchスケジューラーでの定義を行うスケジュールの定義
from apscheduler.schedulers.background import BackgroundScheduler

sched = BackgroundScheduler()


@sched.scheduled_job("interval", minutes=5)
def shedule():
    service = apis.BatchScheduleServise()
    service.scheduleAction()
    print("Schedule action finished.")


import os

# 環境変数でスケジュールフラグがTrueの場合のみスケジュールを設定する。
if os.environ.get("SCHEDULE_FLAG", default=False) == True:
    print("[DEBUG]Schedule job start.")
    sched.start()
