#1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# in -> out
#- 6782 -> 23
#- 0.67 -> 13
#- 198.45 ->27

num = float(input("Введите число: "))
l=len(str(num))-1
new_num=int(num*10**l)
result = 0
while(new_num > 0):
    result += new_num % 10
    new_num //= 10
print("Сумма цифр равна:", result)
      
    