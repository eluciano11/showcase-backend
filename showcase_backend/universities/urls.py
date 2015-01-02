from rest_framework import routers

from .views import UniversityViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'universities', UniversityViewSet)
urlpatterns = router.urls
