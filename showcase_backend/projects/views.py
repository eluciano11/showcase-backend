from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Project
from .serializers import ProjectSerializer, ProjectDepartmentSerializer
from ..users.models import User


class ProjectViewSet(ModelViewSet):
    model = Project
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(created_by=self.request.user)


class ProjectDepartmentListAPIView(ListAPIView):
    model = Project
    serializer_class = ProjectDepartmentSerializer

    def get_queryset(self):
        slug = self.request.slug
        print slug
