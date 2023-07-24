from collections import defaultdict

text = """Lorem ipsum - класичний варіант умовного беззмстовного тексту, що вставляється до філосовського трактату ..."""

def get_word_list(text):
    words_of_text = text.split(" ")
    word_dict = {}
    for word in words_of_text:
        word_dict_value = word_dict.get(word[0])
        if word_dict_value:
            word_dict_value.append(word)
        else:
            word_dict[word[0]] = [word]
    print(word_dict)

get_word_list(text)

def get_word_list_dd(text):
    words_of_text = text.split(" ")
    word_dict = defaultdict(list)
    for word in words_of_text:
        word_dict[word[0]].append(word)
    print(word_dict)

get_word_list_dd(text)
