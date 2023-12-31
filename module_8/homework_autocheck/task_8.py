from collections import Counter

task = """
Есть список IP адресов:
IP = [
    "85.157.172.253",
    ...
]
Реализуйте две функции. Первая get_count_visits_from_ip с помощью Counter будет
возвращать словарь, где ключ — это IP, а значение — количество вхождений в
указанный список.
Пример:
{
    '85.157.172.253': 2,
    ...
}
Вторая функция get_frequent_visit_from_ip возвращает кортеж с наиболее часто
встречаемым в списке IP и количеством его вхождений в список.
Пример:
('66.50.38.43', 4)
"""

IP = [
    "85.157.172.253",
    "85.157.172.253",
    "86.157.172.213",
    "89.157.172.353",
    "81.157.172.245",
    "89.157.172.223",
    "89.157.172.223",
]


def get_count_visits_from_ip(ips):
    print(Counter(ips))
    return Counter(ips)


def get_frequent_visit_from_ip(ips):
    print(Counter(ips).most_common(1)[0])
    return Counter(ips).most_common(1)[0]


get_count_visits_from_ip(IP)
get_frequent_visit_from_ip(IP)
