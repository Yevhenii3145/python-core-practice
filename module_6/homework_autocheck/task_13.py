import shutil
from pathlib import Path

task = """Реализуйте функцию create_backup(path, file_name, employee_residence)
Где:
-path — путь к файлу
-file_name — имя файла
-employee_residence — словарь, в котором ключ — имя пользователя, а его значение — страна
проживания. Вид: {'Michael': 'Canada', 'John':'USA', 'Liza': 'Australia'}
Функция должна работать следующим образом:
-Создавать бинарный файл file_name по пути path
-Сохранять данные словаря employee_residence в файл, где каждая новая строка — это ключ значение
через пробел как 'Michael Canada'
-Архивировать папку по пути path с помощью shutil
-Имя архива должно быть 'backup_folder.zip'
-Функция должна вернуть строку пути к архиву 'backup_folder.zip'
Требования:

-запишите содержимое словаря employee_residence в бинарный файл с именем file_name в папке path
с помощью оператора with.
-используйте символ /, чтобы разделить путь для path и file_name
-вид строки файла — Michael Canada, в конце каждой строки добавляется перевод строки '\n'.
-при сохранении строка файла кодируется методом encode
-при записи строк используем только метод write
-архив должен быть в формате zip с именем 'backup_folder' созданный при помощи make_archive.
"""


path = Path("./task_13")
file_name = ("task_13.txt")

employee = {'Michael': 'Canada', 'John': 'USA', 'Liza': 'Australia'}


def create_backup(path, file_name, employee_residence):
    with open(path / file_name, "wb") as fh:
        for key, value in employee_residence.items():
            string = '{} {}\n'.format(key, value)
            fh.write(string.encode())
        archive_name = shutil.make_archive("backup_folder", "zip", path)
        return archive_name


create_backup(path, file_name, employee)
