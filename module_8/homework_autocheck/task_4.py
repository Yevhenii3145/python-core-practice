from random import randrange

task = """
Для того чтобы выиграть главный приз лотереи, необходимо совпадение нескольких
номеров на лотерейном билете с числами, выпавшими случайным образом и в неком
диапазоне во время очередного тиража. Например, необходимо угадать шесть чисел
от 1 до 49 или пять чисел от 1 до 36 и т.д.
Напишите функцию, которая будет случайным образом подбирать набор чисел для
лотерейного билета. Среди этих чисел не должно быть дубликатов.
Формат функции get_numbers_ticket(min, max, quantity), где параметры:
-min — минимальное значение диапазона, не может быть меньше 1
-max — максимальное значение диапазона, не может быть большее 1000
-quantity — количество чисел в наборе (должен быть min < quantity < max)
Функция должна вернуть список случайных чисел по возрастанию. Если нарушены
условия ограничений на параметры функции, тогда вернуть пустой список.
"""


def get_numbers_ticket(min, max, quantity):
    lottery_list = []
    if min < 1 or max > 1000 or not (min < quantity < max):
        print(lottery_list)
        return lottery_list
    while True:
        if len(lottery_list) == quantity:
            lottery_list = sorted(lottery_list)
            print(lottery_list)
            return lottery_list
        lottery_number = randrange(min, max + 1)
        if lottery_number in lottery_list:
            continue
        lottery_list.append(lottery_number)


get_numbers_ticket(15, 100, 8)  # []
# [17, 19, 22, 23, 48, 52, 53, 55, 58, 67, 69, 73, 74, 75, 77, 79, 92]
get_numbers_ticket(15, 100, 17)
