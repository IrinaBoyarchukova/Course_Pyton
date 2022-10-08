# 1. Задайте строку из набора чисел. Напишите программу,
#    которая покажет большее и меньшее число.
#    В качестве символа-разделителя используйте пробел.
# in 2 19 45 27
# out 2 45
# line = input()
# list_1 = [x.strip(',.*') for x in line.split() if x.replace("-", "").isdigit()]
# print(f'Min: {min(list_1)}')
# print(f'Max: {max(list_1)}')

#__________2______________

line = input()
# list_1 = [int(x.strip(',.*')) for x in line.split() if x.replace("-", "").isdigit()]
list_1 = [x.strip(',.*') for x in line.split() if x.replace("-", "").isdigit()]
print(f'Min: {min(list_1, key=int)}')
print(f'Max: {max(list_1, key=int)}')