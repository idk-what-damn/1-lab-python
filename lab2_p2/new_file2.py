#сгенерировать словарь содержащий не менее 5 элементов, добавить возмодность черз пользовательский ввод добавлять изменять удалять ваш словарь, в итог доожен выводиться файл
import random
with open("file2.txt", "w") as f:
    f.write("")

def cache(func):
    def wrapper(*args):
        result = func(*args)
        with open ("file2.txt", "a") as f:
            f.write(f"{result}\n")
            return result
    return wrapper

@cache
def generate_dict():
    dictonary = {}
    elemets = random.randint(5, 10)
    letters = 'ABCDEFGHIJK'
    for el in range(elemets):
        dictonary[el] = random.choice(letters)
    return dictonary

@cache
def add_to_dict(dictonary, key, value):
    dictonary[key] = value
    return dictonary
@cache
def del_from_dict(dictonary, key):
    del dictonary[key]
    return dictonary


while True:
    print("----МЕНЮ----")
    print("1:Сгенерировать словарь\n2:Добавить в словарь\n3:Удалить из словаря\n4:Просмотреть словарь\n5:Завершить работу")
    choice = int(input("Сделайте ваш выбор: "))
    match choice:
        case 1:
            dictonary = generate_dict()
        case 2:
            key = int(input("Введите ключ для добавления: "))
            value = input("Введите значение для ключа: ")
            dictonary = add_to_dict(dictonary, key, value)
        case 3:
            key2 = int(input("Введите ключ по которому надо удалить: "))
            dictonary = del_from_dict(dictonary, key2)
        case 4:
            print(f"Ваш словарь: {dictonary}")
        case 5:
            print("Работа завершена!")
            break



# dictonary = generate_dict()
# print(dictonary)
# key = int(input("Введите ваш ключ: "))
# value = input("Введите значение для ключа: ")
# dictonary2 = add_to_dict(dictonary, key, value)
# print(dictonary2)
#
# key2 = int(input("Введите ключ для удаления: "))
# dictonary3 = del_from_dict(dictonary, key2)
# print(dictonary3)