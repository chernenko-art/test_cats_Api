# from urllib import request
import requests
import json


def simple_request(url = 'https://cat-fact.herokuapp.com/facts/random'):
    resp = requests.get(url)

    body = resp.content.decode()
    cat_fact_json = json.loads(body)

    return (resp.status_code, resp.headers, cat_fact_json)

status_code, headers, fact_json = simple_request('https://cat-fact.herokuapp.com/facts/random')

print("Code: ", status_code)
print("Headers: ", headers)
print("Json: ", fact_json)
print("Fact: ", fact_json['text'])
