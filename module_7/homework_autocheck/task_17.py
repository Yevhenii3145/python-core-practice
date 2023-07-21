task = """
Вернемся к предыдущей задаче и выполним обратную задачу. Напишите рекурсивную функцию
encode для кодирования списка или строки. В качестве аргумента функция принимает список
( например ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"]) или строку
(например "XXXZZXXYYYZZ"). Функция должна вернуть закодированный список элементов
(пример ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]).
"""
# РЕКУРСИЯ ЭТО ПОЛНЕЙШАЯ ХУЙНЯ


# решение Vasilic
def encode(data):
    if len(data) == 0:
        return []
    index = 1
    while index < len(data) and data[index] == data[index - 1]:
        index += 1
    current = [data[0], index]
    print(current)
    return current + encode(data[index:len(data)])


# решение chat GPT (рекурсия)
def encode_gpt(data):
    def encode_recursive(data, char, count, r_list):
        if not data:
            if char:
                r_list.extend([char, count])
            return r_list

        el = str(data.pop(0))
        if not char:
            char = el
            count = 1
        elif el == char:
            count += 1
        else:
            r_list.extend([char, count])
            char = el
            count = 1

        return encode_recursive(data, char, count, r_list)

    if isinstance(data, str):
        data = list(data)

    return encode_recursive(data.copy(), "", 0, [])
