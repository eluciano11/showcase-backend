from rest_framework.serializers import ModelSerializer

from .models import University


class UniversitySerializer(ModelSerializer):
    class Meta:
        model = University
