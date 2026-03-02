def merge_sorted_list(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1
    if list1[0] <= list2[0]:
        return [list1[0]] + merge_sorted_list(list1[1:], list2)
    else:
        return [list2[0]] + merge_sorted_list(list1, list2[1:])


list_a = list((input("Введите элмеенты для первого списка в строку: ").replace(" ", "")))
list_b = list((input("Введите элементы для второго списка в строку: ").replace(" ", "")))
for item in range(len(list_a)):
    list_a[item] = int(list_a[item])
for item in range(len(list_b)):
    list_b[item] = int(list_b[item])
list_a = sorted(list_a)
list_b = sorted(list_b)

print("Слияние списков:")
print("  Первый список:", list_a)
print("  Второй список:", list_b)

result = merge_sorted_list(list_a, list_b)

print("\nРезультат объединения:")
print("  Отсортированный список:", result)
