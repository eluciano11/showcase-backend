from ..router import SharedAPIRootRouter

from .views import DepartmentViewSet

router = SharedAPIRootRouter(trailing_slash=False)
router.register(r'departments', DepartmentViewSet)
