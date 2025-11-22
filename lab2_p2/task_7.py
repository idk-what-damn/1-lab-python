def merge_sorted_list(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1

    if list1[0] <= list2[0]:
        return [list1[0]] + merge_sorted_list(list1[1:], list2)
    else:
        return [list2[0]] + merge_sorted_list(list1, list2[1:])


list_a = [1, 3, 5, 7]
list_b = [2, 4, 6, 8, 10]

print("Слияние списков:")
print("  Первый список:", list_a)
print("  Второй список:", list_b)

result = merge_sorted_list(list_a, list_b)

print("\nРезультат объединения:")
print("  Отсортированный список:", result)
