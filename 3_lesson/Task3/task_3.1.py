## 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#    Напишите программу, которая определит, присутствует ли в заданном списке число,
#    полученное от пользователя.

from random import sample # sample возьмет последов. и выведит кол-во элементов


def find_num(count, num):
    if count < 0:  # Ввод отрицательно числа
        return " Error:Negative value of the number of numbers!"

    list_nums = sample(range(1, count * 2), count)
    print(list_nums)

    if num in list_nums:
        return f" Yes : The number - {num} is present in the list."
    return f" No : The number - {num} is not in the list."


print(find_num(int(input("Number of numbers: ")), int(input("Number: "))))
