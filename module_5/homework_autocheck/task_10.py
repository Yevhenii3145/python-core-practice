import re


def find_word(text, word):
    match = re.search(f'{word}', text)
    # <re.Match object; span=(34, 40), match='Python'>
    print(match)
    if match:
        return {
            'result': True,
            'first_index': match.span()[0],
            'last_index': match.span()[1],
            'search_string': word,
            'string': text
        }
    else:
        return {
            'result': False,
            'first_index': None,
            'last_index': None,
            'search_string': word,
            'string': text
        }


print(find_word(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
    "Python"))
