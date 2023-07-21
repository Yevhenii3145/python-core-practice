task = """
Разберем простую технику кодирования и декодирования на основе серий. Например, у нас
есть список с повторяющимися наблюдениями какой-то величины, она может принимать
значения X, Y или Z. Значения появляются в произвольном порядке и храним мы их в списке
["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"] или строке "XXXZZXXYYYZZ".

За счет чего мы можем уменьшить объем хранимой информации? Сжатие можно достичь заменой
группы повторяющихся значений на однократное значение и счетчик повторов:
["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]
Напишите рекурсивную функцию decode для декодирования списка, закодированного этим
способом. В качестве аргумента функция принимает закодированный список. Функция должна
вернуть расшифрованный список элементов.
"""


def decode(data):
    char = ""
    r_list = []

    for el in data:
        el = str(el)
        if el.isalpha():
            char = el
        elif el.isdigit():
            count = int(el)
            for _ in range(count):
                r_list.append(char)
            char = ""
    print(r_list)
    return r_list

# решение chat GPT (рекурсия)


def decode_gpt(data):
    def decode_recursive(data, char, r_list):
        if not data:
            return r_list

        el = str(data.pop(0))
        if el.isalpha():
            char = el
        elif el.isdigit():
            count = int(el)
            for _ in range(count):
                r_list.append(char)

        return decode_recursive(data, char, r_list)

    return decode_recursive(data.copy(), "", [])


decode(["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2])
