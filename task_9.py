def get_type_name(obj):
    return obj.__class__.__name__

def type_matches(obj, expected_type):
    return get_type_name(obj) == expected_type.__name__

def type_check(*expected_types):
    def decorator(func):
        def wrapper(*args):
            i = 0
            while i < get_length(args):
                actual = args[i]
                expected = expected_types[i]
                if not type_matches(actual, expected):
                    raise TypeError("Аргумент №" + to_string(i + 1) + " имеет тип '" +
                                    get_type_name(actual) + "', ожидался тип '" +
                                    expected.__name__ + "'")
                i = i + 1
            return func(*args)
        return wrapper
    return decorator

def get_length(seq):
    count = 0
    for _ in seq:
        count = count + 1
    return count

def to_string(x):
    digits = "0123456789"
    if type(x) == int:
        result = ""
        if x == 0:
            return "0"
        while x > 0:
            d = x % 10
            result = digits[d] + result
            x = x // 10
        return result
    return "<?>"

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
try:
    add("3", 5)
except TypeError as e:
    print(e)
