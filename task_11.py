def zodiac_sign(day, month):
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Водолей"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Рыбы"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Овен"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Телец"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Близнецы"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Рак"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Лев"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Дева"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Весы"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Скорпион"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Стрелец"
    else:
        return "Козерог"

try:
    day = int(input("Введите день рождения (1–31): "))
    month = int(input("Введите месяц рождения (1–12): "))

    if 1 <= day <= 31 and 1 <= month <= 12:
        sign = zodiac_sign(day, month)
        print("Ваш знак зодиака: ",sign)
    else:
        print("Некорректная дата. Введите день от 1 до 31 и месяц от 1 до 12.")
except ValueError:
    print("Ошибка ввода: пожалуйста, введите целые числа.")
