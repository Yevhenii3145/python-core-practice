task = """Вернемся к нашей задаче с телефонными номерами. Компания расширяется
и вышла на рынок Азии. Теперь в списке приходят телефоны разных стран. Каждая
страна имеет свой телефонный код .

Компания работает со следующими странами:

Страна	  Код ISO	    Префикс
Japan	    JP	        +81
Singapore	SG	        +65
Taiwan	    TW	        +886
Ukraine	    UA	        +380

Чтобы мы могли корректно выполнить маркетинговую SMS кампанию,
необходимо выдать для каждой страны свой список телефонных номеров.

Напишите функцию get_phone_numbers_for_сountries, которая будет:

1.Принимать список телефонных номеров.
2.Санитизировать (нормализовать) полученный список телефонов клиентов
с помощью нашей функции sanitize_phone_number.
3.Сортировать телефонные номера по указанным в таблице странам.
4.Возвращать словарь со списками телефонных номеров для каждой страны в следующем виде:
{
    "UA": [<здесь список телефонов>],
    "JP": [<здесь список телефонов>],
    "TW": [<здесь список телефонов>],
    "SG": [<здесь список телефонов>]
}
5.Если не удалось сопоставить код телефона с известными, этот телефон должен быть добавлен в список словаря с ключом "UA".
"""


def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


phone_preficses = {
    "JP": "81",
    "SG": "65",
    "TW": "886",
    "UA": "380",
}


def get_phone_numbers_for_countries(list_phones):
    sortered_phones = {}
    for phone in list_phones:
        phone = sanitize_phone_number(phone)
        for key, value in phone_preficses.items():
            if phone.startswith(value):
                if sortered_phones.get(key):
                    values_by_key = sortered_phones.get(key)
                    values_by_key.append(phone)
                    updating_dict = {key: values_by_key}
                    sortered_phones.update(updating_dict)
                else:
                    updating_dict = {key: [phone]}
                    sortered_phones.update(updating_dict)

        if sortered_phones.get("UA"):
            values_by_key = sortered_phones.get("UA")
            values_by_key.append(phone)
            updating_dict = {"UA": values_by_key}
            sortered_phones.update(updating_dict)
            break
        else:
            updating_dict = {"UA": [phone]}
            sortered_phones.update(updating_dict)
    print(sortered_phones)
    return (sortered_phones)


new_list = ["+265678555", "2677-26(46)64", "810000000000",
            "+6500000000000", "886211111111111", "+380222222", "+886999999991", "+38024444444"]
get_phone_numbers_for_countries(new_list)
