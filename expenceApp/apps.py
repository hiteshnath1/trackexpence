from django.apps import AppConfig


class ExpenceappConfig(AppConfig):
    name = 'expenceApp'

    def ready(self):
        import expenceApp.signals  
