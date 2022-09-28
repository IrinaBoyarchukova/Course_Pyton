# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# -------------------------------------- 1 вариант

# num = int(input())
# result = 1

# for i in range(num):
#     print(result, end=", ")
#     result *= -3


# -------------------------------------- 2 вариант

# num = int(input())

# for i in range(num):
#     print((-3) ** i, end=", ")

# ================================== 3 вариант

n = int(input("Введите чиcло N: "))
j = 1
list1 = []
for i in range(1, n + 1):
    list1.append(str(j))
    j *= -3
print(", ".join(list1))

