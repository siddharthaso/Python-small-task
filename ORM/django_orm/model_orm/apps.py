from django.apps import AppConfig


class ModelOrmConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'model_orm'
