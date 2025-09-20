def razbienie(amount):
    result = {}
    result[100] = amount // 100
    amount %= 100
    result[50] = amount // 50
    amount %= 50
    result[10] = amount // 10
    amount %= 10
    result[5] = amount // 5
    amount %= 5
    result[2] = amount // 2
    amount %= 2
    result[1] = amount // 1
    amount %= 1
    return result

my_integer = int(input("Введите ваше число: "))
parts = razbienie(my_integer)
if parts[100]: print(f"100 : {parts[100]}")
if parts[50]: print(f"50 : {parts[50]}")
if parts[10]: print(f"10 : {parts[10]}")
if parts[5]: print(f"5 : {parts[5]}")
if parts[2]: print(f"2 : {parts[2]}")
if parts[1]: print(f"1 : {parts[1]}")