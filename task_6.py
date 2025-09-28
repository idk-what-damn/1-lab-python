def get_length(seq):
    count = 0
    for _ in seq:
        count = count + 1
    return count

def is_list(x):
    try:
        _ = x[0]
        _ = x + []
        return True
    except:
        return False

def contains(seq, value):
    i = 0
    while i < get_length(seq):
        if seq[i] == value:
            return True
        i = i + 1
    return False

def unique_elements(data):
    result = []
    def collect(x):
        i = 0
        while i < get_length(x):
            item = x[i]
            if is_list(item):
                collect(item)
            else:
                if not contains(result, item):
                    result = result + [item]
            i = i + 1
        return result
    return collect(data)

list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2 ,3]]]]

print("Исходный вложенный список:")
print(list_a)

unique = unique_elements(list_a)

print("\nУникальные элементы (в порядке появления):")
print(unique)
