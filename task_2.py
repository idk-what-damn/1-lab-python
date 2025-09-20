stroka = input("Введите строку: ")
if not stroka.strip():
    print("Строка пустая!")
else:
    stroka = stroka.replace("a", '')
    stroka = stroka.replace("e", '')
    stroka = stroka.replace("y", '')
    stroka = stroka.replace("u", '')
    stroka = stroka.replace("i", '')
    stroka = stroka.replace("o", '')
print(stroka)


