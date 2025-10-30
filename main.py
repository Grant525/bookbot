import sys
from stats import num_words
from stats import counter
from stats import sort_on
from stats import dict_list
#   from stats import re_format


def get_book_test(book):
    with open(book) as s:
        book = s.read()
    return book

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    x = get_book_test(sys.argv[1])
    y = num_words(x)
    z = counter(x)
    print(f"Found {y} total words")   
    a = dict_list(z) 
    a.sort(reverse=True,key=sort_on)
    #d = re_format(a)
    for u in a:
        print(f'{u["char"]}: {u["num"]}')

main()  
