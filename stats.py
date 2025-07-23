def count_words(txt):
    num = 0
    text = txt.split()
    for word in text:
        num += 1
    return f"Found {num} total words"

def count_letters(txt):
    abc = {}
    text = txt.split()
    for word in text:
        for letter in word:
            if letter.lower() not in abc:
                abc[letter.lower()] = 0
            abc[letter.lower()] += 1
    return abc

def sort_dict(dic):
    result = []
    for key in dic:
        tmp = {}
        tmp.update({"char": key, "num": dic[key]})
        result.append(tmp)
    result.sort(reverse=True, key=lambda item: item["num"])
    return result

    
