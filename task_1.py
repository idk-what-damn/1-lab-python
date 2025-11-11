fio_string = input("Введите ваше ФИО: ")
words = fio_string.split()

if len(words) == 3:
    print(words[0] + " " + words[1][0] + "." + words[2][0] + ".")
else:
    print("Ошибка: нужно ввести exactly 3 слова (Фамилия Имя Отчество)")