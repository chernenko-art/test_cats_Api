import pytest
from requests import get
import logging
import json


def level_logging():
    """Return level for logging config"""
    json_file = open(
        '/home/chernenkoac/prog/test_cats_api/test_cats_api_python/config.json', 'r').read()
    json_body = json.loads(json_file)
    numeric_level = getattr(logging, json_body["level_loggin"].upper(), None)
    return numeric_level


logging.basicConfig(level=level_logging(),
                    format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='sum.log'
                    )


def test_check_status_code(url):
    """Сheck status_code is `200`"""
    endpoint = '/facts/random?'
    logging.info(f'Run test_check_status_code')
    response = get(url + endpoint)
    logging.info(f'Server response expected = 200, response status code = {response.status_code}')
    assert response.status_code == 200


def test_content_type_header(url):
    """Сheck `application/json` in response body"""
    endpoint = '/facts/random?'
    logging.info(f'Run test_content_type_header')
    response = get(url + endpoint)
    content_type = response.headers['content-type'] # referencing the 'content-type' key
    header_list = [elem.strip() for elem in content_type.split(';')]
    logging.info(f'Server response expected = "application/json", response header result = {header_list}')
    assert 'application/json' in header_list
    

def test_key(url):
    """Сheck keys from documentation in response body"""
    endpoint = '/facts/random?'
    logging.info(f'Run test_key')

    # set the key lists defined in the documentation
    key_list_spec = ['_id', '_v', 'user', 'text', 'updatedAt', 'sendDate',
                    'deleted', 'source', 'type', 'status']
    logging.info(f'Expected list of keys: {key_list_spec}')
    key_list_spec_status = ['verified', 'feedback', 'sentCount']
    logging.info(f'Expected list of keys for "status": {key_list_spec_status}')
    
    # generating lists of actual keys in response
    response = get(url + endpoint)
    key_list_fact = [key.strip() for key in response.json()]
    logging.info(f'Response json list of keys: {key_list_fact}')
    key_list_fact_status = [key.strip() for key in response.json()['status']]
    logging.info(f'Response json list of keys for "status": {key_list_fact_status}')

    # generation of lists of actual keys that are missing from the documentation
    key_error_list = [key for key in key_list_fact \
        if key not in key_list_spec]
    key_error_list_status = [key for key in key_list_fact_status \
        if key not in key_list_spec_status]

    logging.error(f'Response json key are not in the documentation: common - {key_error_list} for status keys - {key_error_list_status}')
    # logic for determining the correspondence of actual documentation keys
    if len(key_error_list) != 0 or len(key_error_list_status) != 0:
        key_list_spec.extend(key_list_spec_status)
        key_error_list.extend(key_error_list_status)
        assert key_list_spec == key_error_list
    else:
        assert True


def test_animal_type(url):
    """Сheck parameter `animal_type` in response body"""
    endpoint = '/facts/random?'
    logging.info(f'Run test_animal_type')
    animal_type_list = ['cat', 'dog', 'snail', 'horse']
    for type in animal_type_list:
        response = get(url + endpoint, params={'animal_type': type})
        data = response.json()
        logging.info(f'Expected animal type = {type}, response animal type = {data["type"]}')
        assert data['type'] == type


def test_amount(url):
    """Сheck facts by `amount` parameter"""
    endpoint = '/facts/random?'
    logging.info(f'Run test_amount')
    amount_list = [2, 250, 500]
    for amount in amount_list:
        response = get(url + endpoint, params={'amount': amount})
        data = response.json()
        logging.info(f'Expected amount = {amount}, response amount = {len(data)}')
        assert len(data) == amount
       
    # checking the conclusion of 1 fact
    response_1_fact = get(url + endpoint, params={'amount': 1})
    data_1_fact = response_1_fact.json()
    logging.info(f'Get amount = 1, expected type response json = dict, response type json = {len(data)}')
    assert type(data_1_fact) == type(dict())

    # Checking negative values
    negative_amount_list = [501, 0, -1]
    for amount in negative_amount_list:
        response_negativ_fact = get(url + endpoint, params={'amount': amount})
        status_code = response_negativ_fact.ok
        logging.error(f'Get negativ amount = {amount}, server response expected = "False", server real response = {status_code}')
        assert status_code == False
       

def test_random_fact(url):
    """Checking the random facts output"""
    endpoint = '/facts/random?'
    logging.info(f'Run test_random_fact')
    facts_list = []
    for _ in range(5):  # conclusion of 5 facts
        response = get(url + endpoint)
        fact = response.json()['text']
        facts_list.append(fact)
    logging.info(f'Expected: unique fact >=1, response: unique facts = {len(set(facts_list))}')
    assert len(set(facts_list)) > 1  # check the uniqueness of at least 1 value
    

def test_id_fact(url):
    """Checking the random facts output by `id`"""
    endpoint = '/facts/'
    logging.info(f'Run test_id_fact')
    id_fact_spec = {'5fd56d1cb3fb8b001735717d': 'Your cat’s grooming process stimulates blood flow to his skin, regulates his body temperature and helps him relax.',
                    '5ff72ed8e54d7b001760c402': 'Cats love eat a meat.',
                    '6094b4be86cf590017ab68b0': 'Cats are the better pets in the world.'
                    }
    for id_key in id_fact_spec.keys():
        response = get(url + endpoint + id_key)
        data = response.json()
        logging.info(f'Expected fact = {id_fact_spec[id_key]}, response fact = {data["text"]}')
        assert data['text'] == id_fact_spec[id_key]
