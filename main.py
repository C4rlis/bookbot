from stats import count_words
from stats import count_letters
from stats import sort_dict
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
def get_book_text(path):
    
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    path_to_book = sys.argv[1]
    text = get_book_text(path_to_book)
    count_words(text)
    counted = count_letters(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(count_words(text))
    print("--------- Character Count -------")
    for d in sort_dict(counted):
        if d.get("char","num").isalpha():
            
            print(f"{d.get("char")}: {d.get("num")}")


    print("============= END ===============")

main()
