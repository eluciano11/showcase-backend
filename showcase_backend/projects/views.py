from rest_framework.viewsets import ModelViewSet

from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(ModelViewSet):
    model = Project
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
