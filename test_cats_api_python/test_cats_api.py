import pytest
from requests import get


def test_check_status_code(url):
    """Сheck status_code is `200`"""
    endpoint = '/facts/random?'
    response = get(url + endpoint)
    assert response.status_code == 200


def test_content_type_header(url):
    """Сheck `application/json` in response body"""
    endpoint = '/facts/random?'
    response = get(url + endpoint)
    content_type = response.headers['content-type'] # referencing the 'content-type' key
    header_list = [elem.strip() for elem in content_type.split(';')]
    assert 'application/json' in header_list
    

def test_key(url):
    """Сheck keys from documentation in response body"""
    endpoint = '/facts/random?'

    # set the key lists defined in the documentation
    key_list_spec = ['_id', '_v', 'user', 'text', 'updatedAt', 'sendDate',
                    'deleted', 'source', 'type', 'status']
    key_list_spec_status = ['verified', 'feedback', 'sentCount']
    
    # generating lists of actual keys in response
    response = get(url + endpoint)
    key_list_fact = [key.strip() for key in response.json()]
    key_list_fact_status = [key.strip() for key in response.json()['status']]

    # generation of lists of actual keys that are missing from the documentation
    key_error_list = [key for key in key_list_fact \
        if key not in key_list_spec]
    key_error_list_status = [key for key in key_list_fact_status \
        if key not in key_list_spec_status]

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
    animal_type_list = ['cat', 'dog', 'snail', 'horse']
    for type in animal_type_list:
        response = get(url + endpoint, params={'animal_type': type})
        data = response.json()
        assert data['type'] == type


def test_amount(url):
    """Сheck facts by `amount` parameter"""
    endpoint = '/facts/random?'
    amount_list = [2, 250, 500]
    for amount in amount_list:
        response = get(url + endpoint, params={'amount': amount})
        data = response.json()
        assert len(data) == amount
    
    # checking the conclusion of 1 fact
    response_1_fact = get(url + endpoint, params={'amount': 1})
    data_1_fact = response_1_fact.json()
    assert type(data_1_fact) == type(dict())

    # Checking negative values
    negative_amount_list = [501, 0, -1]
    for amount in negative_amount_list:
        response_negativ_fact = get(url + endpoint, params={'amount': amount})
        status_code = response_negativ_fact.ok
        assert status_code == False
       

def test_random_fact(url):
    """Checking the random facts output"""
    endpoint = '/facts/random?'
    facts_list = []
    for _ in range(5):  # conclusion of 5 facts
        response = get(url + endpoint)
        fact = response.json()['text']
        facts_list.append(fact)
    assert len(set(facts_list)) > 1  # check the uniqueness of at least 1 value
    

def test_id_fact(url):
    """Checking the random facts output by `id`"""
    endpoint = '/facts/'
    id_fact_spec = {'5fd56d1cb3fb8b001735717d': 'Your cat’s grooming process stimulates blood flow to his skin, regulates his body temperature and helps him relax.',
                    '5ff72ed8e54d7b001760c402': 'Cats love eat a meat.',
                    '6094b4be86cf590017ab68b0': 'Cats are the better pets in the world.'
                    }
    for id_key in id_fact_spec.keys():
        response = get(url + endpoint + id_key)
        data = response.json()
        assert data['text'] == id_fact_spec[id_key]
