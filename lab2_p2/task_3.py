import time

def log_calls(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            current_time = time.localtime()
            formatted_time = (
                str(current_time.tm_year) + "-" +
                str(current_time.tm_mon).zfill(2) + "-" +
                str(current_time.tm_mday).zfill(2) + " " +
                str(current_time.tm_hour).zfill(2) + ":" +
                str(current_time.tm_min).zfill(2) + ":" +
                str(current_time.tm_sec).zfill(2)
            )

            log_line = "Время: " + formatted_time
            log_line += " | Функция: " + func.__name__
            log_line += " | Аргументы: " + str(args)
            if kwargs:
                log_line += " " + str(kwargs)

            with open(filename, "a") as file:
                file.write(log_line + "\n")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log_calls("Lab_2_2/call_log.txt")
def greet(name):
    print(f"Привет, {name}!")

@log_calls("Lab_2_2/call_log.txt")
def add(*args):
    result = sum(args)
    print(f"Сумма: {result}")
    return result

print("Вызов функции greet:")
greet("Boy")

print("Вызов функции add:")
add(7, 5)
