def flat_list(lst):
    i = 0
    while i < list_len(lst):
        if is_list(lst[i]):
            nested = lst[i]
            remove_el(lst, i)
            insert_el(lst, i, nested)
        else:
            i = i + 1

def list_len(seq):
    count = 0
    for _ in seq:
        count += 1
    return count

def is_list(x):
    try:
        _ = x[0]
        _ = x + []
        return True
    except:
        return False

def remove_el(lst, index):
    result = []
    i = 0
    while i < list_len(lst):
        if i != index:
            result = result + [lst[i]]
        i = i + 1
    lst[:] = result

def insert_el(lst, pos, sublist):
    result = []
    i = 0
    while i < pos:
        result = result + [lst[i]]
        i = i + 1
    j = 0
    while j < list_len(sublist):
        result = result + [sublist[j]]
        j = j + 1
    while i < list_len(lst):
        result = result + [lst[i]]
        i = i + 1
    lst[:] = result

test = [1, 2, [3, 4, 5], [3, [4], 7]]
print("Исходный список: ")
print(test)
print("Плоский список: ")
flat_list(test)
print(test)
