length_list = int(input("Введите длинну списка чисел: "))
numbers = []
for i in range(length_list):
    num = input(f"Введите число №{i + 1}: ")
    try:
        number = float(num)
        numbers.append(number)
    except ValueError:
        print("Это не число :(")
unique = []
duplicates = []
for i in range(len(numbers)):
    count = 0
    for j in range(len(numbers)):
        if numbers[i] == numbers[j]:
            count += 1
            if count == 1 and numbers[i] not in unique:
                unique.append(numbers[i])
            elif count > 1 and numbers[i] not in duplicates:
                duplicates.append(numbers[i])
chet = []
nechet = []
for val in numbers:
    if val.is_integer():
        if int(val) % 2 == 0:
            chet.append(int(val))
        else:
            nechet.append(int(val))
negative = [val for val in numbers if val < 0]
plav_point = [val for val in numbers if not val.is_integer()]
sum_div5 = sum(val for val in numbers if val.is_integer() and int(val) % 5 == 0)
max_num = max(numbers)
min_num = min(numbers)

print("Уникальные числа: ", unique)
print("Повторяющиеся числа: ", duplicates)
print("Чётные числа: ", chet)
print("Нечётные числа: ", nechet)
print("Отрицательные числа: ", negative)
print("Числа с плавающей точкой: ", plav_point)
print("Сумма всех чисел кратных 5: ", sum_div5)
print("Самое большое число: ", max_num)
print("Самое маленькое число: ", min_num)