#напистакь что нибудь на тему качалки
import random
class Complex:
    def __init__(self, name, amount_podhod, amount_povtor):
        self.check_amount_of_podhod(amount_podhod)
        self.check_amount_of_povtor(amount_povtor)

        self.name = name
        self.amount_podhod = amount_podhod
        self.amount_povtor = amount_povtor

    def __str__(self):
        return f"Упражнение: {self.name}, Подходы: {self.amount_podhod}, Повторения: {self.amount_povtor}"

    def add_amount_of_podhod(self, amount):
        self.amount_podhod += amount
        return self.amount_podhod

    def add_amount_of_povtor(self, amount):
        self.amount_povtor += amount
        return self.amount_povtor

    def remove_amount_of_podhod(self, amount):
        self.amount_podhod -= amount
        return self.amount_podhod

    def remove_amount_of_povtor(self, amount):
        self.amount_povtor -= amount
        return self.amount_povtor

    @property
    def get_amount_of_podhod(self):
        return self.amount_podhod

    @get_amount_of_podhod.setter
    def get_amount_of_podhod(self, amount):
        self.amount_podhod = amount

    @property
    def get_amount_of_povtor(self):
        return self.amount_povtor

    @get_amount_of_povtor.setter
    def get_amount_of_povtor(self, amount):
        self.amount_povtor = amount

    @classmethod
    def check_amount_of_podhod(cls, amount):
        if amount < 0:
            raise ValueError("Количество подходов не может быть меньше 0!")
        return True

    @classmethod
    def check_amount_of_povtor(cls, amount):
        if amount < 0:
            raise ValueError("Количество повторений не может быть меньше 0!")
        return True

    def doing_exercise(self):
        return f"Выполняю упражнение: {self.name} - {self.amount_podhod} подходов по {self.amount_povtor} повторений"

class BackTrain(Complex):
    def __init__(self, name, amount_podhod, amount_povtor):
        super().__init__(name, amount_podhod, amount_povtor)


class LegTrain(Complex):
    def __init__(self, name, amount_podhod, amount_povtor):
        super().__init__(name, amount_podhod, amount_povtor)

class ArmTrain(Complex):
    def __init__(self, name, amount_podhod, amount_povtor):
        super().__init__(name, amount_podhod, amount_povtor)

class ChestTrain(Complex):
    def __init__(self, name, amount_podhod, amount_povtor):
        super().__init__(name, amount_podhod, amount_povtor)

class Generate:
    LEG_EXERCISE_NAME = ["Жим ногами", "Болгарские выпады", "Ягодичный мостик"]
    ARM_EXERCISE_NAME = ["Подъём на бицепс гантелей", "Тяга косичек на трицепс", "Подъём на бицепс z-видного грифа", "Махи гантелями"]
    BACK_EXERCISE_NAME = ["Тяга нижнего блока", "Тяга верхнего блока", "Поднос штанги к груди"]
    CHEST_EXERCISE_NAME = ["Жим лёжа", "Жим в наклоне", "Жим с гантелями"]

    @classmethod
    def generate_legs(cls, name = None, amount_podhod = None, amount_povtor = None):
        name = name or random.choice(cls.LEG_EXERCISE_NAME)
        amount_podhod = amount_podhod or random.randint(3, 5)
        amount_povtor = amount_povtor or random.randint(8, 15)
        return LegTrain(name, amount_podhod, amount_povtor)

    @classmethod
    def generate_arms(cls, name = None, amount_podhod = None, amount_povtor = None):
        name = name or random.choice(cls.ARM_EXERCISE_NAME)
        amount_podhod = amount_podhod or random.randint(3, 4)
        amount_povtor = amount_povtor or random.randint(10, 20)
        return ArmTrain(name, amount_podhod, amount_povtor)

    @classmethod
    def generate_back(cls, name = None, amount_podhod = None, amount_povtor = None):
        name = name or random.choice(cls.BACK_EXERCISE_NAME)
        amount_podhod = amount_podhod or random.randint(3, 5)
        amount_povtor = amount_povtor or random.randint(8, 12)
        return BackTrain(name, amount_podhod, amount_povtor)

    @classmethod
    def generate_chest(cls, name = None, amount_podhod = None, amount_povtor = None):
        name = name or random.choice(cls.CHEST_EXERCISE_NAME)
        amount_podhod = amount_podhod or random.randint(3, 5)
        amount_povtor = amount_povtor or random.randint(6, 12)
        return ChestTrain(name, amount_podhod, amount_povtor)

chest = Generate.generate_chest()
back = Generate.generate_back()
leg = Generate.generate_legs()
arm = Generate.generate_arms()
exercises = [chest, back, leg, arm]
while True:
    print("----MENU----")
    print("1:Просмотреть все упражнения")
    print("2:Добавить количество подходов")
    print("3:Добавить количество повторений")
    print("4:Выполнить тренировку")
    print("5:Выход")
    try:
        choice = int(input("Введите ваш выбор: "))
    except ValueError:
        print("Пожалуйста введите число!")
        continue
    match choice:
        case 1:
            print("Ваша тренировка: ")
            for i, exercise in enumerate(exercises, 1):
                print(f"{i}. {exercise}")

        case 2:
            print("Добавить подходы: ")
            for i, exercise in enumerate(exercises, 1):
                print(f"{i}. {exercise.name}")

            try:
                ex_num = int(input("Выберите номер упражнения")) - 1
                if 0 <= ex_num < len(exercises):
                    amount = int(input("Сколько подходов добавить?"))
                    exercises[ex_num].add_amount_of_podhod(amount)
                    print(f"Успешно! Теперь {exercises[ex_num].name}: {exercises[ex_num].amount_podhod} подходов")
                else:
                    print("Неверный номер упражнения")
            except ValueError:
                print("Введите число!")

        case 3:
            print("Добавить повторения")
            for i, exercise in enumerate(exercises, 1):
                print(f"{i}. {exercise.name}")

            try:
                ex_num = int(input("Выберите номер упражнения")) - 1
                if 0 <= ex_num < len(exercises):
                    amount = int(input("Сколько повторений добавить?"))
                    exercises[ex_num].add_amount_of_povtor(amount)
                    print(f"Успешно! Теперь {exercises[ex_num].name}: {exercises[ex_num].amount_povtor} подходов")
                else:
                    print("Неверный номер упражнения")
            except ValueError:
                print("Введите число!")

        case 4:
            print("Начало тренировки!")
            for exercise in exercises:
                print(exercise.doing_exercise())
            print("Конец тренировки")

        case 5:
            print("Выход из программы")
            break

        case _:
            print("Неверный выбор! Повторите выбор от 1 до 5")