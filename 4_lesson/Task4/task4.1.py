# 1. Задайте строку из набора чисел. Напишите программу,
#    которая покажет большее и меньшее число.
#    В качестве символа-разделителя используйте пробел.
# in 2 19 45 27
# out 2 45

def check(str_list): # check f проверка
    for i, num in enumerate(str_list):
        str_list[i] = num.strip('.,;:?!')
        if not str_list[i].replace("-", "").isdigit():
            return []
    return str_list


def find_max_min(nums_str: str): # f поиска
    list_nums = nums_str.split()
    right_list = check(list_nums)

    if right_list:
        return min(right_list, key=int), max(right_list, key=int)
    print("The data is incorrect")
    return []


print(*find_max_min(input("Enter the numbers separated by a space: ")))