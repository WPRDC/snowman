from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import  JsonResponse, HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
import redis
import random
import json
import base64

# Create your views here.
@csrf_exempt
def snow_plow_records(request):
    if 'HTTP_AUTHORIZATION' in request.META:
        try:
            auth_b64 = request.META['HTTP_AUTHORIZATION'].split(' ')[1]
        except:
            return (HttpResponse('Unauthorized - malformed credentials', status=401))
        auth_str= base64.b64decode(auth_b64).decode()
        usernanme, password = auth_str.split(':')
        user = authenticate(username=usernanme, password=password)
    else:
        return (HttpResponse('Unauthorized - no credentials', status=401))

    if user is None:
        # On bad authentication
        return(HttpResponse('Unauthorized', status=401))
    else:
        if request.method == 'POST':
            r = redis.StrictRedis(host='localhost', port=6379, db=0)
            r.rpush('snowman_records', request.body.decode())
            return(HttpResponse('Done', status=200))
        else:
            return(HttpResponse('Must use POST request', status=405))