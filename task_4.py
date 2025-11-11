my_integer = int(input("Введите ваше число: "))
amount = my_integer

result_100 = amount // 100
amount %= 100

result_50 = amount // 50
amount %= 50

result_10 = amount // 10
amount %= 10

result_5 = amount // 5
amount %= 5

result_2 = amount // 2
amount %= 2

result_1 = amount // 1
amount %= 1

if result_100: print(f"100 : {result_100}")
if result_50: print(f"50 : {result_50}")
if result_10: print(f"10 : {result_10}")
if result_5: print(f"5 : {result_5}")
if result_2: print(f"2 : {result_2}")
if result_1: print(f"1 : {result_1}")