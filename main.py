from stats import count_words
from stats import count_letters 
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text("books/frankenstein.txt")
    count_words(text)
    count_letters(text)


main()
