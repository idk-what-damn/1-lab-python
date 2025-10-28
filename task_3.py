password_string = input("Введите пароль: ")
match password_string:
    case _ if not password_string.strip():
        print("Строка пустая!")
    case _ if len(password_string) < 16:
            print("Слишком короткий")
    case _ if password_string.isdigit() or password_string.isalpha():
            print("Слишком слабый")
    case _:
        print("Надёжный пароль")

