task = """Есть две строки в разных кодировках - "utf-8" и "utf-16".
Нам необходимо понять, равны ли строки между собой.
Реализуйте функцию is_equal_string(utf8_string, utf16_string),
которая возвращает True, если строки равны между собой, и False — если нет.
"""
a = "Hello world!"
b = "Bye world!"

utf8_a = a.encode("utf-8")
utf16_a = a.encode("utf-16")
utf16_b = b.encode("utf-16")


def is_equal_string(utf8_string, utf16_string):
    return utf8_string.decode('utf-8') == utf16_string.decode('utf-16')


print(is_equal_string(utf8_a, utf16_b))  # False
print(is_equal_string(utf8_a, utf16_a))  # True
