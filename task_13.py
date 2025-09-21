import random

secret_number = random.randint(1, 100)

print("Угадайте число от 1 до 100")

while True:
    try:
        guess = int(input("Ваш вариант: "))
        if guess < secret_number:
            print("Больше!")
        elif guess > secret_number:
            print("Меньше!")
        else:
            print("Поздравляю! Вы угадали число!")
            break
    except ValueError:
        print("Введите целое число.")
