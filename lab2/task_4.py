len1_list = int(input("Введите длинну первого списка чисел: "))
numbers_1 = []
for i in range(len1_list):
    num_1 = input(f"Введите число №{i + 1}: ")
    try:
        number = float(num_1)
        numbers_1.append(number)
    except ValueError:
        print("Это не число :(")
len2_list = int(input("Введите длинну второго списка чисел: "))
numbers_2 = []
for i in range(len2_list):
    num_2 = input(f"Введите число #{i + 1}: ")
    try:
        number = float(num_2)
        numbers_2.append(number)
    except ValueError:
        print("Это не число :(")
common = []
for num in numbers_1:
    if num in numbers_2 and num not in common:
        common.append(num)
uniq_1 = []
for num in numbers_1:
    if num not in numbers_2 and num not in uniq_1:
        uniq_1.append(num)
uniq_2 = []
for num in numbers_2:
    if num not in numbers_1 and num not in uniq_2:
        uniq_2.append(num)
others = []
for num in numbers_1 + numbers_2:
    if num not in common and num not in others:
        others.append(num)
print("Числа которые присутствуют в обоих наборах: ", common)
print("Числа из первого набора, которые отсутсвуют во втором: ", uniq_1)
print("Числа из второго набора, которые отсутсвуют в первом ", uniq_2)
print("Числа из обоих наборов, за исключением, найденных в пункте 1: ", others)