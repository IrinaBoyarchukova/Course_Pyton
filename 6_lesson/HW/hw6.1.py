# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.
# in
# 9
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]
# in
# 10
# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

num_list = [15, 16, 2, 3, 1, 7, 5, 4, 10]

# num_list = [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]

def find (list:num_list ):
    num2_list = [num_list[i] for i in range(1, len(num_list)) if num_list[i] > num_list[i - 1]]
    return num2_list

resalt_list = find(num_list)
print(resalt_list) 