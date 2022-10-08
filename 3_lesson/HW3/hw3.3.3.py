# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#    Без использования: встроенной функции преобразования, строк.
# in
# 88
# out
# 1011000
# in
# 11
# out
# 1011
def conv_bin(num: int):
    list_nums = []

    while num > 0:
        list_nums.insert(0, num % 2)
        num //= 2

    print(*list_nums, sep="") # *list-распаковать; sep=""-не разделяй на пробелы


conv_bin(int(input()))
