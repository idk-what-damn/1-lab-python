len1_list = int(input("Введите длину первого списка чисел: "))
numbers_1 = [float(input(f"Введите число №{i + 1}: ")) for i in range(len1_list)]

len2_list = int(input("Введите длину второго списка чисел: "))
numbers_2 = [float(input(f"Введите число #{i + 1}: ")) for i in range(len2_list)]

set1 = set(numbers_1)
set2 = set(numbers_2)

common = set1 & set2

uniq_1 = set1 - set2

uniq_2 = set2 - set1

others = set1 ^ set2

print("Числа которые присутствуют в обоих наборах:", common)
print("Числа из первого набора, которые отсутствуют во втором:", uniq_1)
print("Числа из второго набора, которые отсутствуют в первом:", uniq_2)
print("Числа из обоих наборов, за исключением найденных в пункте 1:", others)
