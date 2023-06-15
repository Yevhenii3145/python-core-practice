text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
alphabet = "abcdefghijklmnopqrstuvwxyz"
words = []
start = 0
for index, char in enumerate(text):
    if not char.lower() in alphabet:
        word = text[start:index]
        words.append(word)
        start = index + 1
print(words)
