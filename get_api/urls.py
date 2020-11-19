
from rest_framework.routers import DefaultRouter
from get_api.views import PatientInfoViewSet

router = DefaultRouter()
router.register('get-api', PatientInfoViewSet)
urlpatterns = router.urls


