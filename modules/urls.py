from rest_framework.routers import DefaultRouter
from .views import EducationalModuleViewSet

router = DefaultRouter()
router.register(r'modules', EducationalModuleViewSet, basename='educationalmodule')

urlpatterns = router.urls
