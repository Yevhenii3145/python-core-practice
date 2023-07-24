import collections


task = """
У нас есть именованный кортеж для хранения котов в переменной Cat. На первом месте
у нас кличка котика nickname, потом его возраст age и имя владельца кота owner.
Разработайте функцию convert_list(cats), которая будет работать в двух режимах.
Если функция convert_list принимает в параметре cats список именованных кортежей
[Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
То функция вернет следующий список словарей:
[
    {"nickname": "Mick", "age": 5, "owner": "Sara"},
    {"nickname": "Barsik", "age": 7, "owner": "Olga"},
    {"nickname": "Simon", "age": 3, "owner": "Yura"},
]
И в то же время, если функция convert_list принимает в параметре cats список
словарей, то результатом будет обратная операция и функция вернет список
именованных кортежей.
Для определения типа параметра cats используйте функцию isinstance.
"""

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])

cats_namedtuples = [Cat("Mick", 5, "Sara"), Cat(
    "Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
cats_objects = [
    {"nickname": "Mick", "age": 5, "owner": "Sara"},
    {"nickname": "Barsik", "age": 7, "owner": "Olga"},
    {"nickname": "Simon", "age": 3, "owner": "Yura"},
]


def convert_list(cats):
    cats_converted = []
    if isinstance(cats[0], tuple):
        for cat in cats:
            cat_obj = {"nickname": cat.nickname,
                       "age": cat.age,
                       "owner": cat.owner}
            cats_converted.append(cat_obj)
    elif isinstance(cats[0], object):
        for cat in cats:
            print(cat)
            nickname = cat["nickname"]
            age = cat["age"]
            owner = cat["owner"]
            cat_tuple = Cat(nickname, age, owner)
            cats_converted.append(cat_tuple)
    print(cats_converted)
    return cats_converted


convert_list(cats_objects)
convert_list(cats_namedtuples)
