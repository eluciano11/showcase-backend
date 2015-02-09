from ..router import SharedAPIRootRouter

from .views import SearchViewSet

router = SharedAPIRootRouter()
router.register(r'search', SearchViewSet, base_name='search')
