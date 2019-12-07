from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from ..permissions import *
from ..models import *
from ..serializers import *

class ProfileViewSet(viewsets.ModelViewSet):
    """
    Updates and retrieves Product accounts
    """
    queryset = Profile.objects.all()
    authentication_classes = (TokenAuthentication,)
    serializer_class = ProfileSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in []:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def list(self, request):
        user = request.user
        if user:
            profile, created = Profile.objects.get_or_create(user=user)
            return Response(self.serializer_class(profile).data)

        return Response(status=status.HTTP_400_BAD_REQUEST)
