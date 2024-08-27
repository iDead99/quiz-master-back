from django.apps import AppConfig


class ManageQuizmasterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'manage_quizmaster'

    def ready(self) -> None:
        import manage_quizmaster.signals