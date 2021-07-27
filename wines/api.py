from wines.models import Wine
from rest_framework import serializers, viewsets, permissions
from .serializers import WineSerializer

# Wine Viewset


class WineViewSet(viewsets.ModelViewSet):

    permissions_classes = [permissions.IsAuthenticated]

    serializer_class = WineSerializer

    def get_queryset(self):
        return self.request.user.wines.all()

    def perform_create(self, serializer):
        serializers.save(owner=self.request.user)
