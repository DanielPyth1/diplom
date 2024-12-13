from rest_framework import serializers
from .models import EducationalModule

class EducationalModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalModule
        fields = '__all__'
