# 以下でbatchスケジューラーでの定義を行うスケジュールの定義
from apscheduler.schedulers.background import BackgroundScheduler
from django.apps import AppConfig
import os


class StartingActions(AppConfig):
    name = "startingactions"
    verbose_name = "Starting Application"

    def ready(self):
        sched = BackgroundScheduler()
        # 環境変数でスケジュールフラグがTrueの場合のみスケジュールを設定する。
        # 文字列で返却されるため文字列で判定
        if os.environ.get("SCHEDULE_FLAG", default=False) == "True":
            print("[DEBUG]Scheduler read.")
            sched.start()

        @sched.scheduled_job("interval", minutes=5)
        def shedule():
            print("Scheduled job start.")
            from batch import apis

            service = apis.BatchScheduleServise()
            service.scheduleAction()
            print("Scheduled job finish.")

