task = """
Концепция замыкания хорошо ложится под кеширование значений функций.

Итоговой задачей модуля 3 было рекурсивное вычисление чисел Фибоначчи.

Ряд Фибоначчи — это последовательность чисел вида: 0, 1, 1, 2, 3, 5, 8, ...,
где каждое следующее число последовательности получается сложением двух
предыдущих членов ряда.

В общем виде для вычисления n-го члена ряда Фибоначчи нужно вычислить
выражение: Fn = Fn-1 + Fn-2.
Эту задачу можно решить рекурсивно, вызывая функцию, вычисляющую числа
последовательности до тех пор, пока вызов не дойдет до членов ряда меньше
n = 1, где последовательность задана.

Создайте функцию caching_fibonacci(), которая будет обладать кешем с предыдущеми
вычисленными значениями чисел Фибоначчи. Внутри она содержит функцию fibonacci(n),
которая непосредственно и будет вычислять само число Фибоначчи.
Функция caching_fibonacci() возвращает функцию fibonacci

Если число Фибоначчи храниться в словаре cache, то функция fibonacci возвращает
число из кеша. Если его нет в кеше, то мы вычисляем число и помещаем его в кеш,
и возвращаем из функции fibonacci.
"""

# Решение chatGPT:
def caching_fibonacci():
    cache = {0: 0}

    def fibonacci(n):
        if n in cache:
            return cache[n]
        if n in (1, 2):
            result = 1
        else:
            result = fibonacci(n - 1) + fibonacci(n - 2)
        cache[n] = result
        return result

    return fibonacci


fib = caching_fibonacci()

print(fib(10))  # 55
print(fib(7))   # 13
print(fib(6))   # 5
