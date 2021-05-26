# Тестирование API [cat-fact.herokuapp.com](https://cat-fact.herokuapp.com)

 ## Описание

 Функциональное тестирование API [cat-fact.herokuapp.com](https://cat-fact.herokuapp.com) с использованием:

* **`Python`** - [*test_cats_api_python*](https://github.com/chernenko-art/tests_cats_api/blob/main/test_cats_api_python)
* **`Postman`** - [*test_cats_api_postman*](https://github.com/chernenko-art/tests_cats_api/blob/main/test_cats_api_postman)
### Подробности использования указаны в `REDME.md` соответствующего раздела.

*Функциональные автотесты составлены согласно [документации.](https://alexwohlbruck.github.io/cat-facts/docs/)*

## Выявленные баги
* Несоответствие ключевых полей json body фактическим заначениям:
    * ключ '_v' имеет фактический вид '__v'
    * ключи 'used', 'createdAt' отсутствуют в документации
* Некорректная работа функционала вывода количества фактов (amount):
    * при отправлении запроса, с указанием amount <= 0, не выводится сообщение об ошибке (возвращается пустой лист)
