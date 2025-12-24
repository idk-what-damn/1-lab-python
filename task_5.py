word1_string = input("Введите первое слово: ")
word2_string = input("Введите второе слово: ")
if not word1_string.split() and not word2_string.split():
    print("Строки пустые!")
else:
    word1_string = word1_string.replace(" ", "").lower()
    word2_string = word2_string.replace(" ", "").lower()
    letters_1 = list(word1_string)
    letters_2 = list(word2_string)

    is_anagramm = True
    for letter in letters_1:
        if letters_1.count(letter) != letters_2.count(letter):
            is_anagramm = False
            break
    if is_anagramm:
        print("Слова являются анаграммами!")
    else:
        print("Слова не являются анаграммами!")
