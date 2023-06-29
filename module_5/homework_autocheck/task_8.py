grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(students):
    list = []
    num = 0
    for key, value in students.items():
        num += 1
        bal = grades[value]
        str = '{:>4}|{:<10}|{:^5}|{:^5}'.format(num, key, value, bal)
        list.append(str)
    return list


students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}
for el in formatted_grades(students):
    print(el)
