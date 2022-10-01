# 5. **Реализуйте алгоритм перемешивания списка.
#    Без функции shuffle из модуля random.

from random import randrange

num = int(input())
nums_list = list(range(num))
len_list = len(nums_list)

print(nums_list)

for i in range(len_list):
    n_1 = randrange(len_list)
    n_2 = randrange(len_list)
    nums_list[n_1], nums_list[n_2] = nums_list[n_2], nums_list[n_1] # меняем местами с помощью кортежей

print(nums_list)
# 10
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [4, 0, 2, 3, 9, 6, 5, 7, 1, 8]