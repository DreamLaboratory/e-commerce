from django.apps import AppConfig


class AccounatsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "src.apps.accounts"

    def ready(self):
        import src.apps.accounts.signals  # noqa
