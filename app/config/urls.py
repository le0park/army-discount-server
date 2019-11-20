"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from django.conf.urls import url

from django.views.decorators.csrf import csrf_exempt

from graphene_django.views import GraphQLView

from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter

from discountplace.views.user import *
from discountplace.views.place import *
from discountplace.views.like import *
from discountplace.views.favoritelocation import *


#from django.conf import settings

router = SimpleRouter()
router.register(r'likes', LikeViewSet, basename='like')
router.register(r'places', PlaceViewSet, basename='place')
router.register(r'favorites', FavoriteLocationViewSet, basename='favorite')

urlpatterns = [
    url(r'', include(router.urls)), 
    path('admin/', admin.site.urls),
    url(r'^graphql', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    url('', include('social_django.urls', namespace='social')),
    url(r'^register-by-token/(?P<backend>[^/]+)/$', register_by_access_token),
    url('api-token-auth/', views.obtain_auth_token),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

""" Take this comment out to enable DebugToolbar
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
"""
