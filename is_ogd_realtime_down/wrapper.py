import requests
from . import settings
import json


def _check_realtime(content, status_code):
    d = {'is_up': status_code == 200, 'status_code': status_code}

    if status_code == 200:
        if 'timeReal' in content:
            d['realtime'] = True
        else:
            d['is_up'] = None
            if 'timePlanned' in content:
                d['description'] = 'Realtime down'
                d['realtime'] = False
            else:
                d['description'] = 'something wrong, fix something'

    return d

def check_realtime():
    r = requests.get(settings.REALTIME_TEST_URL)
    return _check_realtime(str(r.content), r.status_code)

def check_underground():
    pass
