import pytest
import request

def test_check_status_code():
    status_code, headers, fact_json = request.simple_request()
    assert status_code == 200

# def test_content_type_header():
#     status_code, headers, fact_json = request.simple_request()
#     # headers
#     # Проверить, что в заголовках есть ключ 'Contetn-Type' и он содержит 'application/json'
#     content_type_header = ""
#     # content_type_header = 'application/json'
#     assert content_type_header == 'application/json'
