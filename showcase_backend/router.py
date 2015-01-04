from rest_framework.routers import SimpleRouter, DefaultRouter
from django.conf import settings


def get_api_urls():
    from importlib import import_module
    for app in settings.INSTALLED_APPS:
        if app.startswith('showcase_backend'):
            try:
                import_module(app + '.urls')
            except (ImportError, AttributeError):
                pass

    return SharedAPIRootRouter.shared_router.urls


class SharedAPIRootRouter(SimpleRouter):
    shared_router = DefaultRouter(trailing_slash=False)

    def register(self, *args, **kwargs):
        self.shared_router.register(*args, **kwargs)
        super(SharedAPIRootRouter, self).register(*args, **kwargs)
