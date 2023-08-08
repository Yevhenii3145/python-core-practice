from collections import UserString
task = """Создайте класс NumberString, наследуйте его от класса UserString, определите
для него метод number_count(self), который будет считать количество цифр в строке.
"""


class NumberString(UserString):
    def number_count(self):
        count = 0
        for char in self.data:
            if char.isdigit():
                count += 1
        return count
