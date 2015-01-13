from ..router import SharedAPIRootRouter

from . import views

router = SharedAPIRootRouter()
router.register(r'projects', views.ProjectViewSet)
