from django.conf.urls import patterns, include
from django.utils.module_loading import import_by_path


def get_api_urlpatterns(apps):
    urls = []

    for app in apps:
        dotted_path = 'showcase_backend.{}.urls.urlpatterns'.format(app)
        urls.append((r'', include(import_by_path(dotted_path))))

    return patterns('', *urls)


urlpatterns = get_api_urlpatterns([
    # 'users',
    'universities',
    'departments',
    # 'projects'
])
