from rest_framework.serializers import ModelSerializer

from .models import Project


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project

    def save_object(self, obj, **kwargs):
        obj.created_by = self.context['request'].user
        super(ProjectSerializer, self).save_object(obj, **kwargs)


class ProjectDepartmentSerializer(ModelSerializer):
    class Meta:
        model = Project
