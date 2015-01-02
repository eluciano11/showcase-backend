from rest_framework import routers

from .views import UserViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet)
urlpatterns = router.urls
