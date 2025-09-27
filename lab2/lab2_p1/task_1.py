stroka_string = input("Введите вашу строку: ")
if not stroka_string.split():
    print("Строка пустая!")
else:
    stroka_string = stroka_string.lower()
    words = stroka_string.split()
    duplicates  = []
    unique_words = []
    for i in range(len(words)):
        count = 0
        for j in range(len(words)):
            if words[i] == words[j]:
                count += 1
        if count > 1 and words[i] not in duplicates:
            duplicates.append(words[i])
        elif count == 1 and words[i] not in unique_words:
            unique_words.append(words[i])
    if duplicates:
        print("Повторяющиеся слова: ")
        for word in duplicates:
            count = 0
            for w in words:
                if w == word:
                    count += 1
            print("Слово:", word, "--- встретилось ", count, "раза")
    else:
        print("Повторяющихся слов нет!")
    if unique_words:
        print("Уникальные слова: ")
        for word in unique_words:
            print( word)
    else:
        print("Уникальных слов нет!")