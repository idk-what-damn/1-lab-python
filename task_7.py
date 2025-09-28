def get_length(seq):
    count = 0
    for _ in seq:
        count = count + 1
    return count

def merge_sorted_list(list1, list2):
    i = 0
    j = 0
    merged = []

    len1 = get_length(list1)
    len2 = get_length(list2)

    print("Слияние списков:")
    print("  Первый список:", list1)
    print("  Второй список:", list2)

    while i < len1 and j < len2:
        if list1[i] <= list2[j]:
            merged = merged + [list1[i]]
            i = i + 1
        else:
            merged = merged + [list2[j]]
            j = j + 1

    while i < len1:
        merged = merged + [list1[i]]
        i = i + 1

    while j < len2:
        merged = merged + [list2[j]]
        j = j + 1

    return merged

list_a = [1, 3, 5, 7]
list_b = [2, 4, 6, 8, 10]

result = merge_sorted_list(list_a, list_b)

print("\nРезультат объединения:")
print("  Отсортированный список:", result)
