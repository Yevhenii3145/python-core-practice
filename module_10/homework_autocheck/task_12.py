task = """Создайте класс IDException, который будет наследовать класс Exception.
Также реализуйте функцию add_id(id_list, employee_id), которая добавляет в список
id_list идентификатор пользователя employee_id и возвращает указанный обновленный
список id_list.
Функция add_id будет вызывать собственное исключение IDException, если employee_id
не начинается с '01', иначе employee_id будет добавлен в список id_list
"""


class IDException(Exception):
    def __init__(self, message="Invalid ID format"):
        self.message = message
        super().__init__(self.message)


def add_id(id_list, employee_id):
    if not employee_id.startswith('01'):
        raise IDException("Employee ID must start with '01'")
    id_list.append(employee_id)
    return id_list
