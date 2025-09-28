def cache(func):
    memory = {}

    def wrapper(*args):
        key = make_key(args)

        if key in memory:
            print("Результат найден в кэше для аргументов:", args)
            return memory[key]

        result = func(*args)
        memory[key] = result
        print("Результат вычислен и сохранён в кэш для аргументов:", args)
        return result

    return wrapper

def make_key(args):
    key = ""
    i = 0
    while i < get_length(args):
        key = key + to_string(args[i]) + "_"
        i = i + 1
    return key

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
    if type(x) == str:
        result = ""
        for ch in x:
            result = result + ch
        return result
    return "<?>"

@cache
def slow_add(a, b):
    print("Выполняется сложение", a, "+", b)
    return a + b

print("Первый вызов:")
print("Результат:", slow_add(3, 4))

print("\nВторой вызов с теми же аргументами:")
print("Результат:", slow_add(3, 4))

print("\nТретий вызов с другими аргументами:")
print("Результат:", slow_add(5, 2))
