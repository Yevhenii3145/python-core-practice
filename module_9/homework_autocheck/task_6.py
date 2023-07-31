task = """
Пусть есть строка с числами (в целях упрощения числа только целые), определяющая
какие-то части общего дохода.
Например:
"The resulting profit was: from the southern possessions $ 100, from the northern
colonies $500, and the king gave $1000."

Необходимо реализовать функцию generator_numbers, которая будет парсить строку и
находить все целые числа в ней, и работая как генератор, отдавать указанные числа
при обращении к ней в цикле.

С парсингом строки мы уже сталкивались в задаче модуля 7, когда разбивали
на лексемы арифметическое выражение

Функция generator_numbers(string="") непосредственно распарсивает строку и при помощи
yield возвращает текущее число.
Функция sum_profit(string) суммирует числа, полученные от generator_numbers, и возвращает
общую сумму прибыли из строки.
"""
import re

def generator_numbers(string=""):
    pattern = r'-?\d+'  # Паттерн для поиска целых чисел в строке (может быть со знаком "-" в начале)
    numbers = re.findall(pattern, string)
    for number in numbers:
        yield int(number)

def sum_profit(string):
    total_sum = 0
    for number in generator_numbers(string):
        total_sum += number
    return total_sum
