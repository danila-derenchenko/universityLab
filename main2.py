import random
import time

def search(array, findword):
    start = time.time()
    n = len(array)
    num = -1

    for i in range(n):
        if array[i] == findword:
            num = i
            break
    finish = time.time()
    return (finish - start) * (10 ** 6)

def main():
    text = input("Введите строку: ")
    text = text.lower()
    words = sorted(set(text.split()))

    print("Отсортированный массив слов:", words)

    print("Введите слово для поиска:")
    search_word = input()
    search_word = search_word.lower()

    result = search(array=words, findword=search_word)
    print(result)

main()