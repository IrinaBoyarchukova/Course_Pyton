# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22
# in
# 4
# out
# [4, 2, 4, 9]
# 8

from random import sample 

def find_sum(count):
    if count <= 0:  
        print(" Error")
    sum=0
    index=0  
    list_nums = sample(range(1, count * 2), count) 
    print(list_nums)
    while index < count: 
       sum += list_nums[index]
       index+= 2
    print(f'Cумма элементов списка, стоящих на нечётных позициях(не индексах) {sum}')

a = int(input('Задайте количество элементов в списке: '))
find_sum(a)