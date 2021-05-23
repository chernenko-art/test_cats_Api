from os import read
from _pytest.fixtures import fixture
import pytest
import json


@pytest.fixture()
def url():
    """Return url address"""
    json_file = open('/home/chernenkoac/prog/test_cats_api/test_cats_api_python/config.json', 'r').read()
    json_body = json.loads(json_file)
    schema = json_body['cat-facts']['schema']
    host = json_body['cat-facts']['host']
    port = json_body['cat-facts']['port']
    return f'{schema}://{host}:{port}'
