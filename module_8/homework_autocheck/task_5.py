import random

task = """
Вы проводите розыгрыш кофеварок Bosch среди зарегистрированных пользователей
вашей интернет страницы.
Список зарегистрированных пользователей — это словарь следующего типа:
participants = {
    "603d2cec9993c627f0982404": "test@test.com",
    "603f79022922882d30dd7bb6": "test11@test.com",
    "60577ce4b536f8259cc225d2": "test2@test.com",
    "605884760742316c07eae603": "vitanlhouse@gmail.com",
    "605b89080c318d66862db390": "elhe2013@gmail.com",
}

Ключ словаря — это уникальный идентификатор базы данных MongoDB, а значение — это
email пользователя. Вам необходимо случайным образом отобрать некое количество
победителей розыгрыша.
Создайте функцию get_random_winners(quantity, participants), которая будет
возвращать список уникальных идентификаторов базы данных из словаря participants
количеством quantity. Это будет список победителей
Требования:
-Получите список ключей словаря. (После выполнения метода keys() используйте
преобразование типов)
-Перемешайте полученный список при помощи метода shuffle
-Выберите случайных победителей, используя метод sample.
-Если переданное количество победителей больше количества пользователей
(quantity > len(participants)) — верните пустой список.

Например: вызов get_random_winners(2, participants) случайно может вернуть
список как: ['60577ce4b536f8259cc225d2', '605b89080c318d66862db390'].
"""

participants = {
    "603d2cec9993c627f0982404": "test@test.com",
    "603f79022922882d30dd7bb6": "test11@test.com",
    "60577ce4b536f8259cc225d2": "test2@test.com",
    "605884760742316c07eae603": "vitanlhouse@gmail.com",
    "605b89080c318d66862db390": "elhe2013@gmail.com",
}


def get_random_winners(quantity, participants):
    winners_list = []
    if quantity > len(participants):
        print(winners_list)
        return winners_list
    list_of_keys = list(participants.keys())
    random.shuffle(list_of_keys)
    winners_list = random.sample(list_of_keys, k=quantity)
    print(winners_list)
    return winners_list


get_random_winners(6, participants)  # []

# ['603d2cec9993c627f0982404', '605884760742316c07eae603']
get_random_winners(2, participants)
