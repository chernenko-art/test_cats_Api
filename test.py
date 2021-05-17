import pytest
import requests
import request

# Проверка, что status_code = 200
def test_check_status_code():
    status_code, headers, fact_json = request.simple_request()
    assert status_code == 200

# Проверка, что в заголовках есть ключ 'Contetn-Type' и он содержит 'application/json'
def test_content_type_header():
    status_code, headers, fact_json = request.simple_request()
    content_type = headers['content-type'] #обращение по ключу 'content-type'
    header = content_type
    for elem in content_type.split(';'): #разбиваем строку по символу "";" и итерируемся по возвращенному листу
        if elem.strip() == 'application/json':  # метод sprip убирает пробелы по краям
            header = elem.strip()
    assert header == 'application/json'

# Проверка cуществования всех полей Model (Fact)
def model_fact():
    status_code, headers, fact_json = request.simple_request()
    key_list_spec = ['_id', '_v', 'user', 'text', 'updatedAt',
                     'sendDate', 'deleted', 'source', 'type', 
                     'status.verified', 'status.feedback', 
                     'status.sentCount']
    for key in fact_json:
        assert key in key_list_spec

# Проверка параметра animal_type в Endpoints (Fact)
def animal_endpoints_fact():
    url = 'https://cat-fact.herokuapp.com/facts/random?'
    animal_type_spec = 'cat'
    animal_type_list = ['cat', 'dog', 'snail', 'horse']
    for type in animal_type_list:
        response = requests.get(url, params={'type':type})
        data = response.json()
        assert data['type'] == animal_type_spec

# Проверка параметра amount в Endpoints (Fact)
def amount_endpoints_fact():
    url = 'https://cat-fact.herokuapp.com/facts/random?'
    amount_list = [1, 2, 250, 500]
    for amount in amount_list:
        response = requests.get(url, params={'amount': amount})
        data = response.json()
        assert len(data) == amount

# Проверка рандома вывода фактов по 5 попыткам
def random_fact():
    status_code, headers, fact_json = request.simple_request()
    facts_list = []
    for _ in range(5):
        fact = fact_json['text']
        assert fact in facts_list
        facts_list.append(fact)
        
# Проверка вывода факта по id
def id_fact():
    pass
