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


# Проверка cуществования ключей в теле ответа
def test_key():
    status_code, headers, fact_json = request.simple_request()
    key_list_spec = ['_id', '_v', 'user', 'text', 'updatedAt', 'sendDate',
                    'deleted', 'source', 'type', 'status',
                     'createdAt', '__v', 'used']  # поля 'createdAt', '__v', 'used' - отсутствуют в спецификации
    for key in fact_json:
        assert key in key_list_spec
    
    # Проверка поля 'status'
    key_list_status = ['verified', 'feedback', 'sentCount']
    for key in fact_json['status']:
        assert key in key_list_status


# Проверка параметра animal_type
def test_animal_type():
    url = 'https://cat-fact.herokuapp.com/facts/random?'
    animal_type_list = ['cat', 'dog', 'snail', 'horse']
    for type in animal_type_list:
        response = requests.get(url, params={'animal_type':type})
        data = response.json()
        assert data['type'] == type


# Проверка параметра amount
def test_amount():
    url = 'https://cat-fact.herokuapp.com/facts/random?'
    amount_list = [2, 250, 500]
    for amount in amount_list:
        response = requests.get(url, params={'amount': amount})
        data = response.json()
        assert len(data) == amount
    
    # Проверка вывода 1 факта
    response_1_fact = requests.get(url, params={'amount': 1})
    data_1_fact = response_1_fact.json()
    assert type(data_1_fact) == type(dict())

    # Проверка негативных значений
    negative_amount_list = [501, 0, -1]
    for amount in negative_amount_list:
        response_negativ_fact = requests.get(url, params={'amount': amount})
        status_code = response_negativ_fact.ok
        assert status_code == False
       

# Проверка рандома вывода фактов по 5 попыткам
def test_random_fact():
    facts_list = []
    for _ in range(5):
        status_code, headers, fact_json = request.simple_request()
        fact = fact_json['text']
        assert fact not in facts_list
        facts_list.append(fact)
# Реализовать логику неповторяемости хотя бы 1 элемента

# Проверка вывода факта по id
def test_id_fact():
    url = 'https://cat-fact.herokuapp.com/facts/'
    id_fact_spec = {'5fd56d1cb3fb8b001735717d': 'Your cat’s grooming process stimulates blood flow to his skin, regulates his body temperature and helps him relax.',
                    '5ff72ed8e54d7b001760c402': 'Cats love eat a meat.',
                    '6094b4be86cf590017ab68b0': 'Cats are the better pets in the world.'
                    }
    for id_key in id_fact_spec.keys():
        response = requests.get(url + id_key)
        data = response.json()
        assert data['text'] == id_fact_spec[id_key]
