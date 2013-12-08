import requests
from . import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page
import json

def _test_request():
    r = requests.get(settings.TEST_URL)
    d = {'is_up': r.status_code == 200, 'status_code': r.status_code}
    content = str(r.content)

    if r.status_code == 200:
        if not 'timeReal' in content:
            d['is_up'] = None
            if 'timePlanned' in content:
                d['description'] = 'Realtime down'
            else:
                d['description'] = 'something not right, fix something'

    return d

@cache_page(15 * 60)
def is_up(request):
    d = _test_request()
    return render(request, 'home.html', d)

@cache_page(15 * 60)
def is_up_json(request):
    return HttpResponse(json.dumps(_test_request()), 'application/json')
