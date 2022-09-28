#1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#6 -> да
#7 -> да
#1 -> нет
day_w = int(input("Введите день недели: ")) 
if day_w >= 1 and day_w < 6:
    print("Heт")
elif day_w == 6 or day_w  == 7:
    print("Да ")
else:
    print("Введите цифру от 1 до 7")

# num = int(input())

# if 5 < num < 8:
#     print("Weekend")
# elif 0 < num < 6:
#     print("Workday")
# else:
#     print("It's not a day of the week!")
# num = int(input('Input the number of the day: '))

# while num < 1 or num > 7:
#     num = int(input('Wrong input. Try again here: '))
# else: 
#     if num == 6 or num == 7:
#         print('Yes')
#     else:
#         print('No')

