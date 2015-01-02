from ..router import SharedAPIRootRouter

from .views import UserViewSet

router = SharedAPIRootRouter(trailing_slash=False)
router.register(r'users', UserViewSet)
