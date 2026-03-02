#пользователь вводить 3 цифры а в структуре сохранять какого вида будет треугольник
def cache(func):
    def wrapper(*args, **kwargs):
        code = func(*args, **kwargs)
        with open("cache.txt", "a", encoding="utf-8") as f:
            f.write(f"Стороны {args} -> {code}\n")
        return code
    return wrapper
@cache
def check_trian(a: int, b: int, c: int):
    spisok = [a, b, c]
    max_value = max(spisok)
    min_value = min(spisok)
    new_spisok = spisok.copy()
    new_spisok.remove(max_value)
    last_value = max(new_spisok)
    if last_value + min_value <= max_value:
        return f"Треугольника с такими сторонами {a}, {b}, {c} не существует"
    else:
        if max_value**2 == last_value**2 + min_value**2:
            return "Это прямоугольный треугольник"
        elif max_value**2 > last_value**2 + min_value**2:
            return "Это тупоугольный треугольник"
        elif max_value**2 < last_value**2 + min_value**2:
            return "Это остроугольный треугольник"

while True:
    print("---Меню---")
    choice = int(input("Сделайте выбор\n1:Делать ввод\n2:Завершение работы\nВаш выбор: "))
    if choice == 1:
        a = int(input("Введите первую сторону треугольника: "))
        b = int(input("Введите вторую сторону треугольника: "))
        c = int(input("Введите третью сторону треунольника: "))
        check_trian(a, b, c)
    if choice == 2:
        print("Работа завершена!")
        break