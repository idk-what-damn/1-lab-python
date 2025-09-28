def merge_dict(dict1, dict2):
    for key in get_keys(dict2):
        if key in dict1:
            if is_dict(dict1[key]) and is_dict(dict2[key]):
                merge_dict(dict1[key], dict2[key])
            else:
                dict1[key] = dict2[key]
        else:
            dict1[key] = dict2[key]

def get_keys(d):
    keys = []
    for k in d:
        keys = keys + [k]
    return keys

def is_dict(x):
    try:
        _ = x.items()
        _ = x.keys()
        return True
    except:
        return False

dict_a = {"a": 1, "b": {"c": 1, "f": 4}}
dict_b = {"d": 1, "b": {"c": 2, "e": 3}}
print("Исходный словарь a: ")
print(dict_a)
print("Исходный словарь b: ")
print(dict_b)
merge_dict(dict_a, dict_b)
print("Результат слияния словарей a и b: ")
print(dict_a)