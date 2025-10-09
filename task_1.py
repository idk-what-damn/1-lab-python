import datetime
class Account:
    def __init__(self, currency, owner_id, owner_ref=None):
        self.currency = currency
        self.owner_id = owner_id
        self.balance = 0
        self.owner_ref = owner_ref

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Недостаточно средств")
        self.balance -= amount
        if self.owner_ref:
            self.owner_ref.log_operation(f"Снятие {amount} {self.currency}")

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        self.balance += amount
        if self.owner_ref:
            self.owner_ref.log_operation(f"Пополнение {amount} {self.currency}")
    def __str__(self):
        return f"{self.currency}: {self.balance}"

class Client:
    def __init__(self, client_id, name):
        self.client_id = client_id
        self.name = name
        self.account = {}

    def open_account(self, currency):
        if currency in self.account:
            raise ValueError("Счёт с такой валютой уже есть!")
        self.account[currency] = Account(currency, self.client_id, owner_ref=self)
        self.log_operation(f"Открыт счёт в валюте {currency}")

    def close_account(self, currency):
        if currency  not in self.account:
            raise ValueError("Не удалось получть доступ к счёту")
        del self.account[currency]
        self.log_operation(f"Закрыт счёт в валюте {currency}")

    def get_account(self, currency):
        if currency not in self.account:
            raise ValueError("Не удалось получить доступ к счёту")
        return self.account[currency]

    def statement(self):
        lines = [f"Клиент: {self.name} (ID: {self.client_id})"]
        for acc in self.account.values():
            lines.append(f"Счёт в валюте {acc.currency}: {acc.balance}")
        return "\n".join(lines)

    def log_operation(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(f"history_{self.client_id}.txt", "a", encoding="utf-8") as f:
            f.write(f"{timestamp}: {message}\n")

class BankAccount:
    def __init__(self):
        self.clients = {}
    def create_acc(self, client_id, name):
        if client_id in self.clients:
            raise ValueError("Клиент с таким ID уже существует!")
        self.clients[client_id] = Client(client_id, name)

    def get_client(self, client_id):
        if client_id not in self.clients:
            raise ValueError("Клиент не найден")
        return self.clients[client_id]

    def transfer(self, from_client, from_currency, to_client, to_currency, amount):
        from_acc = from_client.get_account(from_currency)
        to_acc = to_client.get_account(to_currency)
        if from_acc.owner_id != from_client.client_id or  to_acc.owner_id != to_client.client_id:
            raise PermissionError("Нарушение прав доступа!")
        from_acc.withdraw(amount)
        to_acc.deposit(amount)
        from_client.log_operation(f"Перевод {amount} {from_currency} к клиенту {to_client.client_id}")
        to_client.log_operation(f"Получено {amount} {to_currency} от клиента {from_client.client_id}")

bank = BankAccount()
while True:
    print("\n-----МЕНЮ-----")
    print("1.Создать клиента")
    print("2.Открыть счёт")
    print("3.Закрыть счёт")
    print("4.Пополнить счёт")
    print("5.Снять со счёта")
    print("6.Перевести между клиентами")
    print("7.Показать выписку")
    print("8.Выход")
    choice = input("Выберите действие: ")
    try:
        if choice == "1":
            cid = input("Введите ID клиента: ")
            name = input("Введите имя клиента: ")
            bank.create_acc(cid, name)
            print("Аккаунт создан!")

        elif choice == "2":
            cid = input("Введите ваш ID: ")
            currency = input("Введите валюту: ")
            client = bank.get_client(cid)
            client.open_account(currency)
            print("Счёт открыт!")

        elif choice == "3":
            cid = input("Введите ваш ID: ")
            currency = input("Введите валюту: ")
            client = bank.get_client(cid)
            client.close_account(currency)
            print("Счёт закрыт!")

        elif choice == "4":
            cid = input("Введите ваш ID: ")
            currency = input("Введите валюту: ")
            amount = float(input("Введите сумму: "))
            client = bank.get_client(cid)
            acc = client.get_account(currency)
            acc.deposit(amount)
            print("Счёт успешно пополнен!")

        elif choice == "5":
            cid = input("Введите ваш ID: ")
            currency = input("Введите валюту: ")
            amount = float(input("Введите сумму: "))
            client = bank.get_client(cid)
            acc = client.get_account(currency)
            acc.withdraw(amount)
            print("Снятие со счёт выполнено!")

        elif choice == "6":
            from_id = input("Введите ID отправителя: ")
            to_id = input("Введите ID получателя: ")
            from_currency = input("Валюта отправителя: ")
            to_currency = input("Валюта получателя: ")
            amount = float(input("Введите сумму: "))
            from_client = bank.get_client(from_id)
            to_client = bank.get_client(to_id)
            bank.transfer(from_client, from_currency, to_client, to_currency, amount)
            print("Перевод выполнен!")

        elif choice == "7":
            cid = input("Введите ваш ID: ")
            client = bank.get_client(cid)
            print("\n-----ВЫПИСКА-----")
            print(client.statement())

        elif choice == "8":
            print("Выход из программы!")
            break

        else:
            print("Неверный выбор!")
    except Exception as e:
        print(f"Ошибка {e}")
