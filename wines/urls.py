from rest_framework import routers, urlpatterns
from .api import WineViewSet

router = routers.DefaultRouter()
router.register('api/wines', WineViewSet, 'wines')

urlpatterns = router.urls
