from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Project
from .serializers import ProjectSerializer

class ProjectCreate(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_permissions(self):
        if self.request.method != 'GET':
            return [IsAuthenticated()]
        return super().get_permissions()


class ProjectRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_permissions(self):
        if self.request.method != 'GET':
            return [IsAuthenticated()]
        return super().get_permissions()