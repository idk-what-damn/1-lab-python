my_integer = int(input("Введите ваше число: "))

digits = list(map (int, str(my_integer)))

summ = sum(digits)
if summ % 7 ==0:
    print("Магическое число!")
else:
    print(summ)