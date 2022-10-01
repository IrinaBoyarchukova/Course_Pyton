# 2. Задайте список, состоящий из произвольных слов, количество задаёт пользователь.
#    Напишите программу, которая определит индекс второго вхождения строки в списке
#    либо сообщит, что её нет.

# from random import choices
# def list_new(n, word):
#     new_list =[]
#     for i in range(n):
#         a=choices(word,k=3)
#         new_list.append(''.join(a))
#     return new_list

# def list_search(my_list, key):
#     if my_list.count(key) >1:
#         print('Yes')
#         n=my_list.index(key)
#         print(my_list.index(key,n+1))
#     else:
#         print(-1)
# result=list_new(20, "abc")
# print(result)
# list_search(result, input())

#__________________2_____________
from random import choices # Формирование списка слов, зашло количество и слово


def list_rand_words(count: int, alp: str = 'xyz'): # вызываем функцию и передаем число и слово xyz
    words_list = []
    for i in range(count):  # цикл 
        letters = choices(alp, k=3) # хотим , чтобы собирал по 3 буквы
        words_list.append("".join(letters)) # собрать вместе abc
    return words_list # возвращать полученный список


def find_sec(word: str, list_words: list):  # Поиск слова которое ищем во втором списке
    if list_words.count(word) > 1:
        index_w = list_words.index(word)
        print(list_words.index(word, index_w + 1))
    else:
        print(-1)


all_list = list_rand_words(int(input("Number of words: ")))
print(all_list)
find_sec(input("Enter the word: "), all_list)
# Вывод
# ['yzz', 'zzy', 'xyx', 'zyx', 'zzx', 'xyz', 'zxz', 'xyy', 'yyz', 'zxx', 'xyy', 'zyz', 'yxy', 'zzz', 'zxz', 'zyz', 'zyz', 'xyz', 'xzx', 'xyx']
# Enter the word: xyx
# 19
