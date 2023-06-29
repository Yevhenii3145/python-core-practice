def is_spam_words(text, spam_words, space_around=False):
    text = text.lower().replace(",", "").replace(".","")
    arr_text = text.split(" ")
    print(arr_text)
    for word in arr_text:
        if space_around:
            for spam in spam_words:
                if spam.lower() == word:
                    return True
        else:
            for spam in spam_words:
                if spam.lower() in word:
                    return True
    return False
