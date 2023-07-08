task = """Пусть у нас есть текстовый файл, который содержит данные
с месячной заработной платой по каждому разработчику компании.

Пример файла:
Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000

Как видим, структура файла — это фамилия разработчика и значение его
заработной платы, разделенной запятой.
Разработайте функцию total_salary(path) (параметр path - путь к файлу),
которая будет разбирать построчно файл и возвращать общую сумму заработной
платы всех разработчиков компании.
Требования к задаче:

-функция total_salary возвращает значение типа float
-для чтения файла функция total_salary использует только метод readline
-мы пока не используем менеджер контекста with
"""


def total_salary(path):
    total_salary = 0
    fh = open(path, "r")
    while True:
        line = fh.readline()
        if not line:
            break
        salary = float(line.split(",")[1])
        print(salary)
        total_salary += salary
    fh.close()
    print(total_salary)
    return total_salary


total_salary("task_1.txt")
