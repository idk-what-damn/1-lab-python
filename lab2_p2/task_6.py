def unique_elements(data, seen=None):
    if seen is None:
        seen = []
    for item in data:
        if isinstance(item, list):
            unique_elements(item, seen)
        else:
            if item not in seen:
                seen.append(item)
    return seen


list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2 ,3]]]]

print("Исходный вложенный список:")
print(list_a)

unique = unique_elements(list_a)

print("\nУникальные элементы (в порядке появления):")
print(unique)
