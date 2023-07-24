from datetime import datetime

task = """
Разработайте функцию get_str_date(date), которая будет преобразовывать дату из базы
данных в формате ISO "2021-05-27 17:08:34.149Z" в строковое представление "Thursday
27 May 2021" — день недели, число, месяц и год. Преобразованное значение функция
должна вернуть при вызове.
"""


def get_str_date(date):
    date_obj = datetime.strptime(date.split(" ")[0], "%Y-%m-%d")
    print(date_obj.strftime("%A %d %B %Y"))
    return date_obj.strftime("%A %d %B %Y")


get_str_date("2021-05-27 17:08:34.149Z")
