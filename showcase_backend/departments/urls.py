from ..router import SharedAPIRootRouter

from .views import DepartmentViewSet

router = SharedAPIRootRouter()
router.register(r'departments', DepartmentViewSet)
