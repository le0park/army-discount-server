from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..permissions import *
from ..models import *
from ..serializers import *

class PlaceRequestViewSet(viewsets.ModelViewSet):
    """
    Updates and retrieves Product accounts
    """
    queryset = PlaceRequest.objects.all()
    serializer_class = PlaceRequestSerializer

    def get_queryset(self):
        userId = self.request.user.id
        return PlaceRequest.objects.filter(user=userId)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in []:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def create(self, request):
        userId = request.user.id
        request.data['user'] = userId

        return super().create(request)

    def destroy(self, request, pk=None):
        if self.get_queryset().filter(pk=pk).exists():
            return super().destroy(request, pk)
        else:
            return Response({ 'message': 'Invalid.' }, status=status.HTTP_400_BAD_REQUEST)
    


    