from rest_framework.viewsets import ModelViewSet

from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(ModelViewSet):
    model = Project
    serializer_class = ProjectSerializer
    lookup_field = 'id'

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        query_params = self.request.QUERY_PARAMS

        if query_params:
            return Project.objects.filter(created_by=query_params['user'])
        else:
            return Project.objects.all()
