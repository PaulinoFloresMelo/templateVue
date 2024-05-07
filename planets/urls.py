from django.urls import path
from .views import UniverseViewSet, PlanetViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('planets', PlanetViewSet, basename = 'planets' )
router.register('universes', UniverseViewSet, basename = 'universes' )

urlpatterns = router.urls