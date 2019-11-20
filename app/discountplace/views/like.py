from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response

from ..permissions import *
from ..models import *
from ..serializers import *

class LikeViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in []:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    @action(methods=['post'], detail=False, url_path='do')
    def like_or_unlike(self, request):
        userId = request.user.id
        placeId = request.data['place']

        like = Like.objects.filter(user=userId, place=placeId)
        if like.exists():
            return self.unlike(like)
        else:
            request.data['user'] = userId
            return self.like(request.data)

    def unlike(self, queryset):
        deleted = queryset.delete()
        return Response(deleted)

    def like(self, data):
        like = LikeSerializer(data=data)
        like.is_valid()
        like.save()
        return Response(like.data)

    @action(methods=['post'], detail=False, url_path='count')
    def count(self, request):
        placeId = request.data['place']
        likeCount = Like.objects.filter(place=placeId) \
                                .count()
        return Response({ 'count': likeCount })

    

    
