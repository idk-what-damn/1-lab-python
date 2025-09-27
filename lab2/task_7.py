stroka_string = input("Введите вашу строку повторяющихся символов: ")
if not stroka_string.split():
    print("Строка пустая!")
else:
    letters = list(stroka_string)
    compressed = ""
    count = 1
    for i in range(1, len(letters)):
        if letters[i] == letters[i-1]:
            count += 1
        else:
            compressed += letters[i - 1] + str(count)
            count = 1
    compressed += letters[-1] + str(count)
    print("Сжатая строка: ",compressed)


