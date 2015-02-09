import watson

from rest_framework import viewsets
from rest_framework.response import Response

from ..universities.models import University
from ..universities.serializers import UniversitySerializer
from ..projects.models import Project
from ..projects.serializers import ProjectSerializer
from ..users.models import User
from ..users.serializers import UserSimpleSerializer


class SearchViewSet(viewsets.GenericViewSet):
    authentication_classes = ()

    def list(self, request, *args, **kwargs):
        if not 'q' in self.request.QUERY_PARAMS:
            return Response({})
        if 'models[]' in self.request.QUERY_PARAMS:
            models = self.request.QUERY_PARAMS['models[]']
            search_models = []
            if 'University' in models:
                search_models.append(University)
            if 'Project' in models:
                search_models.append(Project)
            if 'User' in models:
                search_models.append(User)
            results = watson.search(
                self.request.QUERY_PARAMS['q'], tuple(search_models))
        else:
            results = watson.search(self.request.QUERY_PARAMS['q'])
        universities = []
        users = []
        projects = []
        for r in results:
            if type(r.object) == University:
                universities.append(UniversitySerializer(r.object).data)
            elif type(r.object) == User:
                users.append(UserSimpleSerializer(r.object).data)
            elif type(r.object) == Project:
                projects.append(ProjectSerializer(r.object).data)
        resp = {}
        if len(universities) > 0:
            resp['universities'] = universities
        if len(projects) > 0:
            resp['projects'] = projects
        if len(users) > 0:
            resp['users'] = users
        return Response(resp)
