from rest_framework.serializers import ModelSerializer

from .models import Project


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project

    def create(self, obj, **kwargs):
        obj['created_by'] = self.context['request'].user
        return super(ProjectSerializer, self).create(obj, **kwargs)


class ProjectDepartmentSerializer(ModelSerializer):
    class Meta:
        model = Project
