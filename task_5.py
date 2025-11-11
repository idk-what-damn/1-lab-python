my_integer = int(input("Введите ваше число: "))
summ = 0
numbers = my_integer
while numbers > 0:
    summ += numbers % 10
    numbers //= 10
if summ % 7 ==0:
    print("Магическое число!")
else:
    print(summ)