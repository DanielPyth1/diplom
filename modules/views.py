from rest_framework.viewsets import ModelViewSet
from .models import EducationalModule
from .serializers import EducationalModuleSerializer

class EducationalModuleViewSet(ModelViewSet):
    queryset = EducationalModule.objects.all()
    serializer_class = EducationalModuleSerializer
