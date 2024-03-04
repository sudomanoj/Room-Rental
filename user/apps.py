from django.apps import AppConfig


# class PollsConfig(AppConfig):
#     name = 'polls'

# apps.py
from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'user'

    def ready(self):
        import user.signals  # Import signals file
