import time

def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        duration = (end - start) * 1000

        duration_str = float_to_string(duration)

        print(" Время выполнения функции", func.__name__, ":", duration_str, "мс")
        return result
    return wrapper

def float_to_string(x):
    whole = int(x)
    frac = x - whole
    digits = "0123456789"

    result = ""
    if whole == 0:
        result = "0"
    else:
        temp = ""
        while whole > 0:
            d = whole % 10
            temp = digits[d] + temp
            whole = whole // 10
        result = temp

    result = result + "."
    i = 0
    while i < 3:
        frac = frac * 10
        digit = int(frac)
        result = result + digits[digit]
        frac = frac - digit
        i = i + 1

    return result

@timing
def slow_task():
    print("Выполняется медленная задача...")
    i = 0
    while i < 1000000:
        i = i + 1
    print("Задача завершена.")

print(" Запуск функции с замером времени:")
slow_task()
