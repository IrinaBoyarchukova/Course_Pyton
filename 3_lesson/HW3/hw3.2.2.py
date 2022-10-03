# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]
# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 16, 4]

from random import sample

def fill_list(count):
    if count <= 0:
        print('Error')
    list_numbers = sample(range(1, count * 3), count)
    return list_numbers

def multip_elements(list):
    new_list_numbers = []
    ind = 0
    length = len(list)
    while ind < length / 2:
        new_list_numbers.append(list[ind] * list[(ind + 1) * -1])
        ind += 1
    if length % 2:
        new_list_numbers.append(list[length // 2])
    print(new_list_numbers)
a = int(input('Write count of elements: '))
my_list = fill_list(a)
print(my_list)
multip_elements(my_list) 