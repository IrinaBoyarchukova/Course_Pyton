# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0,
#    с помощью дополнительных библиотек python. Запросите значения А, В, С 3 раза.
#    Уравнения и корни запишите в файл.
# Результат выводится в файл
# in A=1
# in B=2
# in C=-3
# out 1*x**2+2*x-3
# in A=1
# in B=2
# in C=-3
# out 1*x**2+2*x-3
# in A=5
# in B=6
# in C=-7
# out 5*x**2+6*x-7
from math import sqrt


def roots_equ(a, b, c):
    d = b ** 2 - 4 * a * c
    with open("roots.txt", "a", encoding="utf-8") as my_f:
        my_f.write(f"{a}x ** 2 + {b}x + {c}\n")
        if d > 0 and a:
            my_f.write(f"The first root: {(-b + sqrt(d)) / (2 * a):.2f}\n")
            my_f.write(f"The first root: {(-b - sqrt(d)) / (2 * a):.2f}\n")
        elif d == 0 and a:
            my_f.write(f"The root: {-b / (2 * a):.2f}\n")
        else:
            my_f.write("There are no roots.\n")


# 1 2 -3, 5 6 -7, 8 9 -10
for i in range(3):
    roots_equ(int(input("Enter the coefficient 'a': ")), int(input("Enter the coefficient 'b': ")),
              int(input("Enter the coefficient 'c': ")))

#____________2 вариант ЮлиРжевской функция равно 0_______________
# def sqr_r(a, b, c):
#     d = b ** 2 - 4 * a * c
#     if a == 0:
#         return print('Error')
#     with open('sqr.txt', 'a', encoding='utf-8') as my_f:
#         my_f.write(f'{a}x² + {b}x + ({c}) = 0\n')
#         if d > 0:
#             my_f.write(f'{(-b + sqrt(d)) / (2 * a)}\n')
#             my_f.write(f'{(-b - sqrt(d)) / (2 * a)}\n')
#         elif d == 0:
#             my_f.write(f'{-b / (2 * a)}\n')
#         else:
#             my_f.write('Нет корней\n')


# for i in range(3):
#     sqr_r(int(input('A: ')), int(input('B: ')), int(input('C: ')))
#     print()

        
