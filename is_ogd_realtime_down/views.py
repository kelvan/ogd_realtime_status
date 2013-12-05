import requests
import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page

@cache_page(15 * 60)
def is_down_again(request):
    r = requests.get(settings.TEST_URL)
    d = {'is_up': r.status_code == 200, 'status_code': r.status_code}

    if r.status_code == 200:
        if not 'timeRealtime' in r.content:
            d['is_up'] = None

    return render(request, 'home.html', d)
