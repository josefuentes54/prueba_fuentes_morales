from rest_framework import routers
from .api import CarrerasSerializersViewSet

router = routers.DefaultRouter()
router.register('api/carreras', CarrerasSerializersViewSet, 'carreras')

urlpatterns = router.urls