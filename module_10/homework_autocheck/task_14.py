task = """Реализуйте класс Contacts, который будет работать с контактами. На первом этапе
мы добавим два метода.

list_contacts возвращает список контактов, переменная contacts из текущего экземпляра класса
add_contacts добавляет новый контакт в список, который является переменной
объекта — contacts

Класс Contacts содержит переменную класса current_id. Мы будем использовать ее при
добавлении нового контакта в качестве уникального идентификатора контакта. Когда
мы добавляем новый контакт, то передаем такие аргументы в метод add_contacts:
name, phone, email и favorite. Метод должен создать словарь с указанными ключами и
значениями из параметров функции. Также необходимо добавить в словарь новый ключ id,
значением которого является значение переменной класса current_id.
"""


class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        contact = {
            'id': Contacts.current_id,
            'name': name,
            'phone': phone,
            'email': email,
            'favorite': favorite
        }
        self.contacts.append(contact)
        Contacts.current_id += 1
