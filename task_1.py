stroka_string = input("Введите вашу строку: ")

if not stroka_string.strip():
    print("Строка пустая!")
else:
    words = stroka_string.lower().split()

    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    print("\nСловарь слов и их количества:")
    for word, count in word_counts.items():
        print(f"{word}: {count}")

    unique_count = len(word_counts)
    print(f"\nКоличество уникальных слов: {unique_count}")
