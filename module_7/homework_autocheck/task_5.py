import re
task = """
Очень часто люди в своих сообщениях не ставят заглавные буквы, особенно это
стало массовым явлением в эру мобильных устройств. Разработайте функцию
capital_text, которая будет принимать на вход строку с текстом и возвращать
строку с восстановленными заглавными буквами.
Функция должна:
-сделать заглавной первую букву в строке, несмотря на пробелы
-сделать заглавной первую букву после точки, несмотря на пробелы
-сделать заглавной первую букву после восклицательного знака, несмотря на пробелы
-сделать заглавной первую букву после вопросительного знака, несмотря на пробелы
"""


# Первый вариант решения
def do_title(char):
    return char.group().title()


def capital_text_1(s):
    normalised_str = re.sub(r"(?:^|\.|\!|\?)\s*([a-z])", do_title, s)
    return normalised_str


# Второй вариант решения
def capital_text(s):
    result_string = ""
    to_change = True
    for ch in s:
        if ch in "!?.":
            to_change = True
            result_string += ch
        elif ch not in "!?. " and to_change:
            ch = ch.upper()
            to_change = False
            result_string += ch
        else:
            result_string += ch
    return result_string
