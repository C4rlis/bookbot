def count_words(txt):
    num = 0
    text = txt.split()
    for word in text:
        num += 1
    print(f"{num} words found in the document")

def count_letters(txt):
    abc = {}
    text = txt.split()
    for word in text:
        for letter in word:
            if letter.lower() not in abc:
                abc[letter.lower()] = 0
            abc[letter.lower()] += 1
    print(abc)
def sort_dict(dic):
    pass
