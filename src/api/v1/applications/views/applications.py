from rest_framework.generics import ListAPIView

from ..models import Application
from ..serializers import ApplicationSerializer


class UserApplicationGet(ListAPIView):
    model = Application
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Application.objects.prefetch_related("job").filter(user=user)
        return queryset
