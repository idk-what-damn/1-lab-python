def get_type_name(obj):
    return obj.__class__.__name__

def type_matches(obj, expected_type):
    return isinstance(obj, expected_type)

def type_check(*expected_types):
    def decorator(func):
        def wrapper(*args):
            def check_recursive(index):
                if index >= len(args):
                    return
                actual = args[index]
                expected = expected_types[index]
                if not type_matches(actual, expected):
                    raise TypeError(
                        f"Аргумент №{index+1} имеет тип '{get_type_name(actual)}', "
                        f"ожидался тип '{expected.__name__}'"
                    )
                check_recursive(index + 1)

            check_recursive(0)
            return func(*args)
        return wrapper
    return decorator


@type_check(int, int)
def add(a, b):
    print("Результат сложения:", a + b)

@type_check(str, int)
def repeat(text, times):
    print("Результат повторения:", text * times)


print("Вызов add(3, 5):")
add(3, 5)

print("Вызов repeat('Hi', 3):")
repeat("Hi", 3)

print("Вызов add('3', 5):")
add("3", 5)   # здесь сразу выбросится TypeError
