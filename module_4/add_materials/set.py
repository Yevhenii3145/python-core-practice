text = "What is Lorem Ipsum? \
Lorem Ipsum is simply dymmy text of the printing and typesetting industry.\
Lorem Ipsum had been the industry's standard dummy text ever since the 1500s,\
when an unknown printer took a galley of type and scramled it to make a type\
specimen book. It has survived not only five centuries, but also the leap into\
elecronic typesetting, remainig essentially unchanged.\
It was popularise in the 1960s with the release of Letraset sheets containing\
Lorem Ipsum passages, and more recently with desktop publishing software like\
Aldus PageMaker including versions of Lorem Ipsum."

alphabet = "abcdefghijklmnopqrstuvwxyz"

char_set = set()
symol_set = set()

for el in text:
    if el.lower() in alphabet:
        char_set.add(el)
    else:
        symol_set.add(el)

print(f"Chars {char_set}")
print(f"Symbols {symol_set}")
