from collections import deque

task = """
LIFO (англ. last in, first out, «последним пришёл — первым ушёл») — способ
организации данных или другими словами Стек ( Stack). В структурированном линейном
списке, организованном по принципу LIFO, элементы могут добавляться и выбираться
только с одного конца, называемого «вершиной списка». Структура LIFO может быть
проиллюстрирована следующей картинкой.
С помощью коллекции deque реализуйте структуру данных LIFO. Создайте переменную
lifo, содержащую коллекцию deque. Ограничьте ее размер с помощью константы MAX_LEN.
Функция push добавляет значение element в начало списка lifo. Функция pop достает
и возвращает первое значение из списка lifo.
"""

MAX_LEN = 10
lifo = deque(maxlen=MAX_LEN)


def push(element):
    lifo.appendleft(element)


def pop():
    return lifo.popleft()

# Либо можно было


def push_r(element):
    lifo.append(element)


def pop_r():
    return lifo.pop()
