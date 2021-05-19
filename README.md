 # Автотесты API [cat-fact.herokuapp.com](https://cat-fact.herokuapp.com)

 ## Описание

 Программа позволяет производить автоматическое функциональное тестирование API [cat-fact.herokuapp.com](https://cat-fact.herokuapp.com) с использованием следующего набора **автотестов**:

* `test_check_status_code()` - проверка статус кода
* `test_content_type_header()` - проверка наличия 'application/json'
* `test_key()` - проверка cуществования ключевых полей в теле ответа
* `test_animal_type()` - проверка поля animal_type
* `test_amount()` - проверка правильности вывода количества фактов
* `test_random_fact()` - проверка рандомного вывода фактов
* `test_id_fact()` - проверка вывода факта по id
## Запуск и использование

*! Автотесты реализованы при помощи **`Python3`**. Для корректной работы кода, необходима установка библиотек `pytest`, `requests`.*

Для запуска автотеста необходимо ввести команду **$ pytest** в *terminal* (*в bash используйте команду `pytest-3`*):
* Запустить все тесты: 
``` 
$ pytest <MODULE> 
```
* Запустить определенный тест: 
``` 
$ pytest <MODULE>::<TEST_NAME> 
```

Ниже представлен пример работы функции **проверки статус кода**:

* *Определение функции*

```python
def test_check_status_code():
    status_code, headers, fact_json = request.simple_request()
    assert status_code == 200
```
* *Запуск теста (осуществляется через модуль `pytest`)* 
```
chernenkoac@DESKTOP-HJKEQ8G:~/prog/test_cats_api$ pytest-3 test_function.py::test_check_status_code
====================== test session starts ======================
platform linux -- Python 3.8.5, pytest-4.6.9, py-1.8.1, pluggy-0.13.0
rootdir: /home/chernenkoac/prog/test_cats_api
collected 1 item                                                                                         
test_function.py .
[100%]
=====================  1 passed in 1.96 seconds ======================
```
*Функциональные автотесты составлены согласно [документации.](https://alexwohlbruck.github.io/cat-facts/docs/)*