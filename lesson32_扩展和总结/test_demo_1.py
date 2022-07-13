import requests
import pytest


def visit_api(method, url, json):
    resp = requests.request(method=method,
                            url=url,
                            json=json)
    return resp.json()


def test_real_world():
    expected = 2
    actual = visit_api('post',
                       'http://httpbin.org/post',
                       {"name": "yuz"})
    assert expected == actual