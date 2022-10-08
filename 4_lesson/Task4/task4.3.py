# 3. Задайте два числа. Напишите программу, которая найдёт
#    НОК (наименьшее общее кратное) этих двух чисел.
# https://zaochnik.com/spravochnik/matematika/delimost/naimenshee-obschee-kratnoe-nok/

# from math import gcd
# def nok(a, b):
#     return (a * b) // gcd(a, b)
# # 14 18 -> 126, 17 11 -> 187
# print(nok(int(input()), int(input())))

#___________2________
from math import gcd
a=int(input("a= "))
b=int(input("b= "))
# 14 18 -> 126, 17 11 -> 187
print(a * b // gcd(a, b))