palindrom_string = input("Введите строка котрая может быть палиндромом: ")
if not palindrom_string.strip():
    print("Строка пустая!")
else:
    cleaned = palindrom_string.replace(" ", "").lower()
    if cleaned == cleaned[::-1]:
        print("Строка является палиндромом!")
    else:
        print("Срока не является палиндромом!")
