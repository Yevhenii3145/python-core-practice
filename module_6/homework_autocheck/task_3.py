task = """В предыдущей задаче мы записали сотрудников в файл в следующем виде:
Robert Stivenson, 28
Alex Denver, 30
Drake Mikelsson, 19
Выполним теперь обратную задачу и создадим функцию read_employees_from_file(path),
которая будет читать данные из файла и возвращать список сотрудников в виде:
['Robert Stivenson, 28', 'Alex Denver, 30', 'Drake Mikelsson, 19']
Помните про присутствие символа конца строки \n при чтении данных из файла. Его необходимо
убирать при добавлении прочитанной строки в список.
Требования:
-прочтите содержимое файла, используя режим "r".
-мы пока не используем менеджер контекста with
-верните из функции список сотрудников из файла
"""


def read_employees_from_file(path):
    employee_list = []
    fh = open(path, "r")
    while True:
        line = fh.readline()
        if not line:
            break
        line = line.replace("\n", "")
        employee_list.append(line)
    fh.close()
    print(employee_list)
    return(employee_list)


read_employees_from_file("task_2.txt")
