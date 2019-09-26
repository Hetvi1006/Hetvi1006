from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals
from import_export import resources
from .models import Feedback

class FeedbackResource(resources.ModelResource):
    class Meta:
        model = Feedback