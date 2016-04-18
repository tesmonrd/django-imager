from django.apps import AppConfig


class ImagerProfileConfig(AppConfig):
    name = 'imager_profile'

    def ready(self):
        """Code to run when the app is ready."""
        from imager_profile import handlers
