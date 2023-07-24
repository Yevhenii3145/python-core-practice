from decimal import Decimal, getcontext

task = """
Создайте функцию decimal_average(number_list, signs_count), которая будет
вычислять среднее арифметическое типа Decimal с количеством значащих цифр
signs_count.
number_list — список чисел
Внимание
Не забывайте приводить все числа в списке к типу `decimal`
Пример:
-вызов функции decimal_average([3, 5, 77, 23, 0.57], 6) вернет 21.714
-вызов функции decimal_average([31, 55, 177, 2300, 1.57], 9) вернет 512.91400
"""


def decimal_average(number_list, signs_count):
    getcontext().prec = signs_count
    sum_numbers = Decimal(0)
    for num in number_list:
        sum_numbers += Decimal(str(num))

    mean = Decimal(str(sum_numbers)) / len(number_list)
    print(mean)
    return mean


decimal_average([3, 5, 77, 23, 0.57], 6)
decimal_average([31, 55, 177, 2300, 1.57], 9)
