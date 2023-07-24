from collections import Counter

text = """By default, the configuration uses SQLite.
If you're new to databases, or you're just interested in trying Django,
this is the easiest chice. SQLite is included in Python,
so you won't need to install anything else to support your database.
When starting your first real project, however,
you may want to use a more scalable database like PostgreSQL,
to avoid database-swithcing headaches down the road."""

def get_count_chars(text):
    count_dict = {}
    for char in text:
        char_in_dict_counter = count_dict.get(char)
        if char_in_dict_counter:
            count_dict[char] = char_in_dict_counter + 1
        else:
            count_dict[char] = 1
    print(count_dict)

get_count_chars(text)

counter = Counter(text)

print("Counter", counter)
print(counter.most_common(5)) # [(' ', 58), ('e', 37), ('t', 34), ('a', 29), ('o', 26)]
print(sorted(counter)) # ['\n', ' ', "'", ',', '-', '.', 'B', 'D', 'I', 'L', 'P', 'Q', 'S', 'W', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'y']
