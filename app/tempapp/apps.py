from django.apps import AppConfig


class tempappConfig(AppConfig):
    name = 'tempapp'

    def ready(self):
        import tempapp.signals
