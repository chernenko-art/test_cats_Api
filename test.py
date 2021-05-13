import pytest
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
        if elem.strip() == 'application/json':
            header = elem.strip()
    assert header == 'application/json'
