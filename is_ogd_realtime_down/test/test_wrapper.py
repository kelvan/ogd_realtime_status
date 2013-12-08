import os
from is_ogd_realtime_down import wrapper

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

def test_500():
    d = wrapper._check_realtime('', 500)
    assert d['is_up'] == False
    assert d['status_code'] == 500

def test_404():
    d = wrapper._check_realtime('Not Found', 404)
    assert d['is_up'] == False
    assert d['status_code'] == 404

def test_realtime():
    with open(os.path.join(DATA_DIR, 'monitor_unicode_real.json')) as f:
        content = f.read()
    d = wrapper._check_realtime(content, 200)
    assert d['is_up'] == True
    assert d['realtime'] == True
    assert d['status_code'] == 200

def test_no_realtime():
    with open(os.path.join(DATA_DIR, 'monitor_no_real.json')) as f:
        content = f.read()
    d = wrapper._check_realtime(content, 200)
    assert d['is_up'] is None
    assert d['realtime'] == False
    assert d['status_code'] == 200
