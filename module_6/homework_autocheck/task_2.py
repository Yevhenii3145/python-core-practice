task = """В компании существует несколько отделов. Список сотрудников
для каждого отдела имеет такой вид:
['Robert Stivenson,28', 'Alex Denver,30']
Это список строк с фамилией и возрастом сотрудника, разделенными запятыми.
Реализуйте функцию записи данных о сотрудниках компании в файл, чтобы информация
о каждом сотруднике начиналась с новой строки.
Функция записи в файл write_employees_to_file(employee_list, path), где:
-path - путь к файлу.
-employee_list - список со списками сотрудников по каждому отделу, как в примере ниже:
[['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]
Требования:
-запишите содержимое employee_list в файл, используя режим "w".
-мы пока не используем менеджер контекста with
-каждый сотрудник должен быть записан с новой строки — т.е для предыдущего списка содержимое
файла должно быть следующим:

Robert Stivenson,28
Alex Denver,30
Drake Mikelsson,19
"""
example = [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]
target_path = "task_2.txt"

def write_employees_to_file(employee_list, path):
    fh = open(path, "w", encoding="utf-8")
    for department in employee_list:
        for employee in department:
            fh.write(f"{employee}\n")
    fh.close()

write_employees_to_file(example,target_path)
