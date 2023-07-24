from datetime import datetime

task = """
Разработайте функцию get_days_from_today(date), которая будет возвращать количество
дней от текущей даты, где параметр date — это строка формата '2020-10-09'
(год-месяц-день).
Подсказки:
-Параметр date разбить на год, месяц и день можно, используя метод строк split.
-datetime принимает аргументы типа int, используйте преобразование типов.
-игнорируйте часы, минуты и секунды для вашей даты, важны полные дни.
-количество дней вы можете получить вычитанием из текущей даты, заданной в date
(без времени).
Например: Если текущая дата — 5 мая 2021, то вызов get_days_from_today("2021-10-09")
вернет нам -157.
"""


def get_days_from_today(date):
    date_now = datetime.now().date()
    (year, month, day) = date.split("-")
    tartget_date = datetime(
        year=int(year), month=int(month), day=int(day)).date()
    difference = date_now - tartget_date
    print(difference.days)
    return difference.days


get_days_from_today("2023-11-05")
