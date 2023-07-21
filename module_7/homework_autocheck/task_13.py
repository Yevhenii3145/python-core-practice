task = """
Есть файл со списком сотрудников компании. В каждой строке файла записана
информация только про одного сотрудника. Формат записи, в учебных целях,
упрощенный в виде имени сотрудника, символа пробела и его должности, т.е.
кем он работает.

John courier
Pipe cook
Создайте функцию get_employees_by_profession(path, profession). Функция должна в файле
(параметр path) найти всех сотрудников указанной профессии (параметр profession)

Требования:
-откройте файл при помощи with для чтения.
-получите строки из файла при помощи метода readlines()
-с помощью метода find найдите все строки в файле, где есть указанная profession,
и поместите записи в список.
-объедините все эти строки в списке в одну строку при помощи метода join (помните
про перевод строк '\n' и лишние пробелы, которые надо убрать).
-уберите значение 'profession' (замените на пустую строку "" при помощи метода
replace).
-верните итоговую строку из файла
"""


def get_employees_by_profession(path, profession):
    employees = []
    with open(path, "r") as fh:
        lines = fh.readlines()
        for line in lines:
            if line.find(profession) != -1:
                employe = line.replace(profession, "").strip()
                employees.append(employe)
        employees_str = " ".join(employees)
        print(employees_str)
        return employees_str


get_employees_by_profession("task_13.txt", "cap")
