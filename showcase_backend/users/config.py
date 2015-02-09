import watson

from django.apps import AppConfig


class UsersConfig(AppConfig):

    name = 'showcase_backend.users'
    verbose_name = 'Users'

    def ready(self):
        watson.register(
            self.get_model('User'))
