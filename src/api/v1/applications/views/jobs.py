from rest_framework import viewsets, permissions


from ..models import Job
from ..serializers.jobs import JobSerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.select_related("header").all()
    serializer_class = JobSerializer
    http_method_names = ["get", "post", "put", "delete"]
    permission_classes = [permissions.IsAuthenticated]
