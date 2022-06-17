from django.apps import AppConfig


class InsuranceConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'insurancePersonalizationAndRecommendation.insuranceProducts'

    def ready(self):
        from .jobs import runapscheduler
        runapscheduler.ScheduleUpdater.start()
