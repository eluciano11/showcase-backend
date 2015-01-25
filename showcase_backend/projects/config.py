from django.apps import AppConfig

import watson


class ProjectsConfig(AppConfig):

    name = 'showcase_backend.projects'
    verbose_name = 'Projects'

    def ready(self):
        watson.register(self.get_model('Project'))
