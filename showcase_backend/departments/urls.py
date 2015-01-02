from rest_framework import routers

from .views import DepartmentViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'departments', DepartmentViewSet)
urlpatterns = router.urls
