import requests
import settings
from django.http import HttpResponse
from django.shortcuts import render

@cache
def is_down_again(request):
    r = requests.get(settings.TEST_URL)
    if r.status_code == 200:
        return HttpResponse('NO')
    else:
        return HttpResponse('YES (%s)' % r.status_code)
