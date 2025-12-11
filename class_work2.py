# написать класс сотрудники. экземпляр класса с аргументами: имя, должность, стаж.
# методы: приходить на работу, уходить с работы, выыполнять задачи, получать зп.
# обязательно прописать какую-то свою ошибку.
# пользовательский ввод: добавить сотрудника, выбрать его действие (ушел с работы, пришел на работу)
class Employee:
    def __init__(self, name, position, experience):
        self.name = name
        self.position = position
        self.experience = experience
        self.is_at_work = False
        self.task_completed = 0

    def come_to_work(self):
        if self.is_at_work:
            print(f"{self.name} уже на работе")
        else:
            self.is_at_work = True
            print(f"{self.name} пришел на работую Должность {self.position}")

    def leave_work(self):
        if not self.is_at_work:
            print(f"{self.name} уже не на работе")
        else:
            self.is_at_work = False
            print(f"{self.name} ушел с работы")

    def perform_task(self, num_tusk):
        if not self.is_at_work:
            raise EmployeeError(f"{self.name} не может выполнять задания, так как не на работе")
        if num_tusk <= 0:
            raise ValueError("Количество задач должно быть положительным")

        self.task_completed += num_tusk
        print(f"{self.name} выполнил {num_tusk}, суммарно выполнено {self.task_completed} задач")

    def get_money(self):
        base_balance = 5000
        experience_bonus = self.experience * 200
        task_bonus = self.task_completed * 100

        total_money = base_balance + experience_bonus + task_bonus
        print(f"{self.name} получил запрлату в размере {total_money}")

        self.task_completed = 0
        return total_money

class EmployeeError(Exception):
    pass

employees = {}
while True:
    print("----МЕНЮ----")
    print("1:Добавить нового сотрудника")
    print("2:Выбрать действие для сотрудника")
    print("3:Показать всех сотрудников")
    print("4:Выйти")
    choice = int(input("Выберите ваше действие: "))
    match choice:
        case 1:
            name = input("Введите имя сотрудника: ")
            position = input("Введите его должность: ")
            try:
                experience = int(input("Введите стаж в годах: "))
                if experience < 0 or experience > 100:
                    print("Стаж не может быть меньше 0 и больше 100!")
                    experience = 0
            except ValueError:
                print("Неверное значение для стажа")
                experience = 0
            employee = Employee(name, position, experience)
            employees[name] = employee
            print(f"Сотрудник {name} добавелен")
        case 2:
            if not employees:
                print("Нет добавленных сотрудников")
                continue
            print("Список сотрудников:")
            for i, name in enumerate(employees.keys(), 1):
                print(f"{i}. {name}")
            try:
                emp_choice = int(input("Выберите номер сотрудника: ")) - 1
                employee_name = list(employees.keys())[emp_choice]
                employee = employees[employee_name]

                print(f"Выбран сотрудник: {employee.name}")
                print(f"На работе: {"ДА" if employee.is_at_work else "НЕТ"}")

                print("Доступные действия: ")
                print("1:Прийти на работу")
                print("2:Уйти с работы")
                print("3:Выполнить задачу")
                print("4:Получить зарплату")
                action = int(input("Выберите действие"))

                match action:
                    case 1:
                        employee.come_to_work()
                    case 2:
                        employee.leave_work()
                    case 3:
                        try:
                            tasks = int(input("Сколько задач выполнить?"))
                            employee.perform_task(tasks)
                        except ValueError:
                            print("Ошибка значения")
                    case 4:
                        employee.get_money()

                    case _:
                        print("Неверный выбор")
            except ValueError:
                print("Некорректный выбор")

        case 3:
            if not employees:
                print("Нет добавленных сотрудников")
            else:
                print("Список всех сотрудников")
                for employee in employees.values():
                    print(f"{employee.name}: {employee.position}, стаж {employee.experience} лет")
                    print(f"На работе {"ДА" if employee.is_at_work else "НЕТ"}")

        case 4:
            print("Выход из программы")
            break

        case _:
            print("Неверный выбор действия")
