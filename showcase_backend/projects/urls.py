from ..router import SharedAPIRootRouter

from .views import ProjectViewSet

router = SharedAPIRootRouter(trailing_slash=False)
router.register(r'projects', ProjectViewSet)
