def get_numbers(x):
    numbers = []
    for i in range(x):
        num = i ** 2
        if not num % 2:
            numbers.append(num)
    print(numbers)


def get_numbers_comprehension(x):
    numbers_list = [i ** 2 for i in range(x) if not i % 2]
    # [0, 4, 16, 36, 64, 100, 144, 196, 256, 324] <class 'list'>
    print(numbers_list, type(numbers_list))
    numbers_set = {i ** 2 for i in range(x) if not i % 2}
    # {0, 64, 256, 4, 36, 100, 196, 324, 16, 144} <class 'set'>
    print(numbers_set, type(numbers_set))
    numbers_dict = {f"{i}^2": i ** 2 for i in range(x) if not i % 2}
    # {'0^2': 0, '2^2': 4, '4^2': 16, '6^2': 36, '8^2': 64, '10^2': 100, '12^2': 144, '14^2': 196, '16^2': 256, '18^2': 324} <class 'dict'>
    print(numbers_dict, type(numbers_dict))


get_numbers(20)
get_numbers_comprehension(20)
