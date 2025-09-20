my_integer = int(input("Введите ваше число: "))
b = []
while  my_integer > 0:
    b.append(my_integer % 10)
    my_integer = my_integer // 10
    b = b[::1]
    summ = sum(b)

if summ % 7 ==0:
    print("Магическое число!")
else:
    print(summ)