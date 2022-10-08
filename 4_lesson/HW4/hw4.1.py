# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
# out
# 9.000000
# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001
# out
# 8.988

from decimal import Decimal


def accuracy(num, acc):
    number = Decimal(f"{num}")
    return number.quantize(Decimal(f"{acc}"))


print(accuracy(float(input("Введите число: ")), float(input("Введите точность округления в формате 0.0001: "))))

#_2вар"
num = float(input('Enter a real number: '))

_, accu = input("Enter the required accuracy '0.0001': ").split(".")
print(f"{num:.{len(accu)}f}")

