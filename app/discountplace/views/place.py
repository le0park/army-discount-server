from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..permissions import *
from ..models import *
from ..serializers import *

class PlaceViewSet(viewsets.ModelViewSet):
    """
    Updates and retrieves Product accounts
    """
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['list', 'retrieve',]:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    