user_list = int(input("Введите длинну списка: "))
elements = []
for i in range(user_list):
    el = input(f"Введите элемент #{i + 1}: ")
    elements.append(el)
uniq_elements = []
for i in range(len(elements)):
    count = 0
    for j in range(len(elements)):
        if elements[i] == elements[j]:
            count += 1
    if count == 1:
        uniq_elements.append(elements[i])
print("Список без дубликатов: ", uniq_elements)