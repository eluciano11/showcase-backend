from ..router import SharedAPIRootRouter

from .views import ProjectViewSet

router = SharedAPIRootRouter()
router.register(r'projects', ProjectViewSet)
