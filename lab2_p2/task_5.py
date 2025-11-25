def cache(func):
    memory = {}
    def wrapper(*args):
        key = args
        if key in memory:
            print("Результат найден в кэше для аргументов:", args)
            return memory[key]
        result = func(*args)
        memory[key] = result
        print("Результат вычислен и сохранён в кэш для аргументов:", args)
        return result
    return wrapper

# def make_key(args):
#     return "_".join(str(arg) for arg in args)

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
