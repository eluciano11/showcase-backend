from ..router import SharedAPIRootRouter

from .views import UniversityViewSet

router = SharedAPIRootRouter()
router.register(r'universities', UniversityViewSet)
