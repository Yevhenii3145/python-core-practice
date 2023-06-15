text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
dict_counter = {}  # {"L": 1, "o": 2}
for char in text:
    # try:
    #     # получаем значение по ключу
    #     count = dict_counter[char]
    # except KeyError:
    #     count = 0
    count = dict_counter.get(char, 0)
    count += 1
    # записываем значение по ключу
    dict_counter[char] = count

print(dict_counter)
