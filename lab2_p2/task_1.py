def flat_list(lst):
    result = []
    for el in lst:
        if isinstance(el, list):
            result.extend(flat_list(el))
        else:
            result.append(el)
    return result

test = [1, 2, [3, 4, 5], [3, [4], 7]]
print("Исходный список: ")
print(test)
print("Плоский список: ")
print(flat_list(test))

