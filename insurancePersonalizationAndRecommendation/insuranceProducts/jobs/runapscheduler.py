from django.conf import settings
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler


class SchedularApi:
    @staticmethod
    def schedule_api():
        """
        Implement the function to schedule
        """
        pass


class ScheduleUpdater():

    @staticmethod
    def start():
        scheduler = BackgroundScheduler()
        """
        we can schedule jobs with intervals mentioned below time config from settings, if we want start from specific 
        time to start the scheduler we can use the parameter  next_run_time=datetime(2022, 6, 16, 15, 38, 20, 0)
        """
        scheduler.add_job(SchedularApi.schedule_api, 'interval', seconds=settings.SCHEDULE_SECONDS,
                          minutes=settings.SCHEDULE_MINUTES, hours=settings.SCHEDULE_HOURS, days=settings.SCHEDULE_DAYS)
        scheduler.start()
