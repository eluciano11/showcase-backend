from ..router import SharedAPIRootRouter

from .views import UniversityViewSet

router = SharedAPIRootRouter(trailing_slash=False)
router.register(r'universities', UniversityViewSet)
