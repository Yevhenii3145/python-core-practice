task = """У вашей компании есть блог. И надо реализовать функцию find_articles
для поиска по статьям нашего блога. Есть список articles_dict, в котором находится
описание статей блога. Каждый элемент этого списка представляет собой словарь со
следующими ключами: фамилии авторов – ключ "author", название статьи – ключ "title",
год издания – ключ "year".Реализуйте функцию find_articles,Параметр key функции
определяет сочетание букв для поиска. Например, при key="Python" функция определяет,
имеются ли в списке articles_dict статьи, в названии или именах авторов которых
встречается это сочетание букв. Если такие элементы списка были найдены, то надо вернуть
новый список из словарей, содержащий фамилии авторов, название и год издания всех таких
статей.Второй ключевой параметр функции letter_case определяет, учитывается ли при поиске
регистр букв, по умолчанию он равен False и регистр не имеет значения т.е.
"Python" и "python" это одно и тоже в тексте. Иначе искать полное совпадение."""

articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]

def find_articles(key, letter_case=False):
    if letter_case == False:
        key = key.lower()
    new_dict= []
    for article in articles_dict:
        for value in article.values():
            if letter_case == False:
                value = str(value).lower()
            if key in str(value):
                new_dict.append(article)
    return(new_dict)

print(find_articles("planets", True)) # [{'title': 'Oceans of other planets are full of silver', 'author': 'Artur Clark', 'year': 2020}]
print(find_articles("Planets", True)) # []
