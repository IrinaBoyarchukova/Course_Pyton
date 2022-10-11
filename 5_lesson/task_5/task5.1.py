# 1. Создайте список из N натуральных чисел(0 до N), 
#    упорядоченных по возрастанию. Среди чисел не хватает
#    одного, чтобы выполнялось условие A[i] - 1 = A[i-1].  
#    Найдите это число.
# in 10
# out 0,1,2,3,4,5,6,7,8,9,10
# 9
# in 10
# out 1,2,3,4,5,6,7,8,9,10
# -1


# from random import choice


# def sequ(num):
#     if num < 1:
#         return []

#     num_list = list(range(num + 1))
#     num_list.remove(choice(num_list))
#     return num_list


# def lostie(num_list):
#     for i in range(1, len(num_list)):
#         if num_list[i - 1] != num_list[i] - 1:
#             return num_list[i] - 1
#     return -1


# list_nums = sequ(int(input()))
# print(list_nums)
# print(lostie(list_nums))

#_________Марина Судакова_________
from random import choice

def fill_list(count: int):
    my_list = [x for x in range(count + 1)]
    my_list.remove(choice(my_list))
    return my_list

new_list = (fill_list(int(input('Write count: '))))
print(new_list)

def find(my_list: list):
    for i in range(1, len(my_list)):
        if my_list[i] - 1 != my_list[i-1]:
            return my_list[i] - 1
    return -1

print(find(new_list))