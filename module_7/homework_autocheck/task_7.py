task = """
В четвертом модуле мы решали задачу нормализации данных. Давайте расширим ее.
При анализе данных часто возникает необходимость избавиться от экстремальных значений,
прежде чем начать работать с данными дальше. Напишите функцию data_preparation, которая
принимает набор данных, список списков (Пример: [[1,2,3],[3,4], [5,6]]). Функция должна
удалять из переданных списков наибольшее и наименьшее значение, но только если размер
списка больше двух элементов. После удаления данных из каждого списка, необходимо слить
их вместе в один список, отсортировать его в порядке убывания и вернуть полученный
список в качестве результата (Для примера выше результат будет следующим: [6, 5, 4, 3, 2]).
"""


def data_preparation(list_data):
    extended_list = []
    for single_list in list_data:
        if len(single_list) > 2:
            max_digit = max(single_list)
            min_digit = min(single_list)
            single_list.remove(max_digit)
            single_list.remove(min_digit)
            extended_list.extend(single_list)
            continue
        extended_list.extend(single_list)
    extended_list.sort()
    extended_list.reverse()
    print(extended_list)
    return extended_list
