import re

text = "First sentence. Second sentence. Third sentence"
sentences = re.split(r"[\.\!\?]", text)
print(sentences)  # ['First sentence', ' Second sentence', ' Third sentence']

text = "First sentence.\nSecond sentence.\nThird sentence"
print(text)
sentences = text.split("\n")
new_text = "$".join(sentences)
print(new_text)  # First sentence.$Second sentence.$Third sentence
