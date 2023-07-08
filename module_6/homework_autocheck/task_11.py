task = """Реализуйте функцию get_credentials_users(path), которая возвращает
список строк из бинарного файла, созданного в предыдущей задаче, где:
-path - путь к файлу.
Формат файла:
andry:uyro18890D
steve:oppjM13LL9e
Откройте файл для чтения, используя with и режим rb. Сформируйте список строк из
файла и верните его из функции get_credentials_users в следующем формате:
['andry:uyro18890D', 'steve:oppjM13LL9e']
Требования:
-Используйте менеджер контекста для чтения из файла
"""


def get_credentials_users(path):
    with open(path, "rb") as fh:
        file = fh.read().decode("utf-8")
        list = file.split("\n")
        list.pop()
    print(list)
    return list


get_credentials_users("task_10.txt")
