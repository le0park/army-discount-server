from django.http.response import HttpResponse
from django.conf import settings

# Create your views here.
from django.contrib.auth import login
import urllib
import json
from social_django.utils import psa
from rest_framework.authtoken.models import Token

# Define an URL entry to point to this view, call it passing the
# access_token parameter like ?access_token=<token>. The URL entry must
# contain the backend, like this:
#
#   url(r'^register-by-token/(?P<backend>[^/]+)/$',
#       'register_by_access_token')

@psa('social:complete')
def register_by_access_token(request, backend):
    # This view expects an access_token GET parameter, if it's needed,
    # request.backend and request.strategy will be loaded with the current
    # backend and strategy.
    req = urllib.request.Request('https://accounts.google.com/o/oauth2/token?grant_type=authorization_code&client_id=%s&client_secret=%s&code=%s&redirect_uri=http://8dosanai.com:8888/complete/google-oauth2/'
                                % (settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY, settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET, request.GET.get('auth_code'))
                            , method='POST')

    try:
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        resp = json.loads(resp_json)
    except Exception as e:
        return HttpResponse(e)

    if not resp:
        return HttpResponse("no response from models API")

    if 'access_token' not in resp:
        return HttpResponse(resp)
    
    user = request.backend.do_auth(resp['access_token'])
    if user:
        login(request, user)
        token, _ = Token.objects.get_or_create(user=user)
        return HttpResponse(token.key)
    else:
        return HttpResponse('ERROR')