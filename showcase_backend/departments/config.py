from django.apps import AppConfig

# import watson


class DepartmentsConfig(AppConfig):

    name = 'showcase_backend.departments'
    verbose_name = 'Departments'

    # def ready(self):
    #     watson.register(self.get_model('Department'))
