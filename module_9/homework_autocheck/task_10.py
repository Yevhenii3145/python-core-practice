task = """
Есть список contacts, элементы которого — словари контактов следующего вида:
{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}
Словарь содержит имя пользователя, его email, телефонный номер и свойство —
избранный контСоздайте функцию get_favorites(contacts), которая будет возвращать
список, содержащий только избранные контакты. Используйте при этом функцию filter,
чтобы отфильтровать по полю favorite только избранные контакты.
"""

def get_favorites(contacts):
    return list(filter(lambda x: x.get("favorite") == True, contacts))
