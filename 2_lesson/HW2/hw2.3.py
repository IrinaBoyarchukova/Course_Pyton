# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13
n = int(input("Введите n: "))
new_list=[]
sum=0
for i in range(1,n+1):
    new_list.append(round((1 + 1 / i)**i))
    sum += new_list[i-1]
print(new_list)
print(sum)