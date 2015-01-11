from rest_framework.viewsets import ModelViewSet

from .models import University
from .serializers import UniversitySerializer


class UniversityViewSet(ModelViewSet):
    model = University
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    lookup_field = 'slug'
