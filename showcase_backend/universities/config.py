import watson

from django.apps import AppConfig


class UniversitiesConfig(AppConfig):

    name = 'showcase_backend.universities'
    verbose_name = 'Universities'

    def ready(self):
        watson.register(
            self.get_model('University'))
