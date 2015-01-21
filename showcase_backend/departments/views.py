from rest_framework.viewsets import ModelViewSet

from .models import Department
from .serializers import DepartmentSerializer


class DepartmentViewSet(ModelViewSet):
    model = Department
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    lookup_field = 'slug'
