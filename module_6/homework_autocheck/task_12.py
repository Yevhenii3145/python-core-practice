import base64


task = """Функция get_credentials_users из предыдущей задачи возвращает
нам список строк username:password:
['andry:uyro18890D', 'steve:oppjM13LL9e']
Реализуйте функцию encode_data_to_base64(data), которая принимает в параметре
data указанный список, выполняет кодирование каждой пары username:password в формат
Base64 и возвращает список с закодированными парами username:password в виде:
['YW5kcnk6dXlybzE4ODkwRA==', 'c3RldmU6b3Bwak0xM0xMOWU=']
"""

list_users = ['andry:uyro18890D', 'steve:oppjM13LL9e']


def encode_data_to_base64(data):
    encoded_data = []
    for item in data:
        item_bytes = item.encode("utf-8")
        item_64bytes = base64.b64encode(item_bytes)
        base64_item_64bytes = item_64bytes.decode("utf-8")
        print(base64_item_64bytes)
        encoded_data.append(base64_item_64bytes)

    print(encoded_data)
    return encoded_data


encode_data_to_base64(list_users)
