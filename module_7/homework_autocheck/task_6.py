task = """
Все вы, возможно, сталкивались с ребусами "Найди слово". Они существуют как текстовые
варианты, так и программы для мобильных приложений. Напомним кратко суть ребуса. В
большом квадрате с набором букв необходимо найти слово по горизонтали и, иногда, по
вертикали.
Реализуйте функцию solve_riddle(riddle, word_length, start_letter, reverse=False)
для нахождения искомого слова в строке ребуса.
Параметры функции:

-riddle - строка с зашифрованным словом.
-word_length - длина зашифрованного слова.
-start_letter - буква, с которой начинается слово (подразумевается, что до начала слова
буква не встречается в строке).
-reverse - указывает, в каком порядке записано слово. По умолчанию — в прямом. Для
значения True слово зашифровано в обратном порядке, к примеру, в строке mi1rewopret
зашифровано слово power.
"""


def solve_riddle(riddle, word_length, start_letter, reverse=False):
    if reverse:
        riddle = riddle[::-1]
    start_i = riddle.find(start_letter)
    if start_i == -1:
        return ""
    last_i = start_i + word_length
    target_word = riddle[start_i:last_i]
    return target_word
