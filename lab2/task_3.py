length_list = int(input("Введите длинну списка чисел: "))
numbers = []
for i in range(length_list):
    num = input(f"Введите число №{i + 1}: ")
    try:
        number = float(num)
        numbers.append(number)
    except ValueError:
        print("Это не число :(")
uniq_nums = []
for num in numbers:
    if num not in uniq_nums:
        uniq_nums.append(num)
if len(uniq_nums) < 2:
    print("Количество уникальных чисел недостаточно!")
else:
    max1 = max2 = float("-inf")
    for num in uniq_nums:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
    print("Второе по велечине число: ", max2)



