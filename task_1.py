def count_words(text):
        if not text.strip():
            return "Строка пустая!"
        word = text.split()
        return len(word)
fio_string = input("Введите ваше ФИО: ")
words = fio_string.split()
if count_words(fio_string) != 3:
    pass
else:
        print(words[0] + " " + words[1][0] + "." +  words[2][0] + ".")