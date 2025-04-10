from django.apps import AppConfig


class MatrixAuthConfigApp(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "matrix_auth_app"

    def ready(self):
        import matrix_auth_app.signals  
