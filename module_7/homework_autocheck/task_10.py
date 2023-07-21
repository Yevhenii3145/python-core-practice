task = """
При работе веб-сервисов общение по протоколу HTTP чаще всего происходит в формате JSON.
И отправка данных на сервер при POST запросе — это необходимость использовать словарь,
так как структура формата JSON идентична словарю Python.
Реализуйте вспомогательную функцию, которая будет формировать запрос на сервер в виде
словаря. Данная функция make_request(keys, values) принимает два параметра в виде списков.
Функция должна создать словарь с ключами из списка keys и значениями из списка values.

-Порядок соответствия совпадает с индексами списков keys и data.
-Если длина keys и values не совпадают, верните пустой словарь.
"""


def make_request(keys, values):
    if len(keys) != len(values):
        return {}
    # через dict comprehension можно:
    # result_dict = {key:value for key,value in  zip(keys,values)}
    result_dict = dict(zip(keys, values))
    return result_dict
