from rest_framework import viewsets

from .models import Department
from .serializers import DepartmentSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    model = Department
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    lookup_field = 'slug'
