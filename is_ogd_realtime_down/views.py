import requests
import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from . import wrapper


@cache_page(15 * 60)
def is_up(request):
    d = wrapper.check_realtime()
    return render(request, 'home.html', d)

@cache_page(15 * 60)
def is_up_json(request):
    return HttpResponse(json.dumps(wrapper.check_realtime()), 'application/json')
