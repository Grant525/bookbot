
def num_words(book):
    words = book.split()
    return len(words)

def counter(book):
    counter = {}
    for symbol in book:
        if symbol.lower() in counter:
            counter[symbol.lower()]+=1 
        else: 
            counter[symbol.lower()] = 1
    return counter

def sort_on(counter):
    return counter["num"]

def dict_list(count):
    list = []
    for key,value in count.items():
        if key.isalpha():
            dict = {"char": key, "num": value}
            list.append(dict)
    return list

