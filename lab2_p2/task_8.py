import time

def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        duration = (end - start) * 1000
        print(f"Время выполнения функции {func.__name__}: {duration:.3f} мс")
        return result
    return wrapper

@timing
def slow_task():
    print("Выполняется медленная задача...")
    i = 0
    while i < 1000000:
        i += 1
    print("Задача завершена.")

print("Запуск функции с замером времени:")
slow_task()
