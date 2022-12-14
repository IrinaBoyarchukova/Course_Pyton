# -*- coding: utf-8 -*-

# -- Sheet --

#f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30

 #Построить график

from sympy import *
# from sympy.abc import x, y, f, g
#from sympy import Symbol, sin, cos

from sympy.plotting import plot

init_printing()

x = Symbol('x')
f = -12 * x ** 4 * sin (cos (x)) - 18 * x ** 3 + 5 * x**2 +10 * x -30
a = plot(f, (x, -7.5, 5))

#Определить корни
solveset(f, x)

#Найти интервалы
b = [-oo, oo]
b[1:1] = solveset(diff(f), x)
b

# Найти интервалы, на которых функция возрастает
# Найти интервалы, на которых функция убывает

c = []
d = []
for i in range(1, len(b)):
    boo = is_increasing(f, Interval.open(b[i-1], b[i]))
    if boo:
        c.append(f"{b[i-1]} {b[i]}")
    else:
        d.append(f"{b[i-1]} {b[i]}")
print('Возрастает в диапазоне', c)
print('Убывает в диапазоне', d)

#  Вычислить вершину
#Экстремумы функции
e = solveset(diff(f), x)
for i in e:
    g = f.subs(x, i)
    if g < 0:
        print(f'Нижний экстремум: x:{i} y:{g}')
    elif g > 0:
        print(f'Верхний экстремум: x:{i} y:{g}')
a = plot(f, (x, -7, 4))

# Определить промежутки, на котором f > 0
# Определить промежутки, на котором f < 0
#Знакопостоянства функции
m = [-oo, oo]

incr_list = []
decr_list = []
m[1:1] = solveset(f, x)
for i in range(1, len(m)):
    boo = is_increasing(f, Interval.open(m[i-1], m[i]))
    if boo:
        incr_list.append(f'{m[i-1]}, {m[i]}')
    else:
        decr_list.append(f'{m[i-1]}, {m[i]}')

# print(f'{0}{1}{2}{3}{0}', *h)

print("f > 0:", *incr_list, sep="\n")
print("f < 0:", *decr_list, sep="\n")

