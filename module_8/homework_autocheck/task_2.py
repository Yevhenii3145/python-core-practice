from datetime import date

task = """
Напишите функцию для определения количества дней в конкретном месяце. Ваша функция
должна принимать два параметра: month — номер месяца в виде целого числа в диапазоне
от 1 до 12 и year — год, состоящий из четырех цифр. Убедитесь, что функция корректно
обрабатывает февраль високосного года.
"""


def get_days_in_month(month, year):
    date_came = date(year=year, month=month, day=1)
    if month == 12:
        year += 1
        month = 0
    date_month_later = date(year=year, month=month + 1, day=1)
    diff = date_month_later - date_came
    print(diff.days)
    return (diff.days)


get_days_in_month(7, 2023)
print(11 / 12)
