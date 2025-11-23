def combine_dicts(dict1, dict2):
    result = dict1.copy()  # Создаем копию первого словаря
    result.update(dict2)   # Обновляем значениями из второго словаря
    return result