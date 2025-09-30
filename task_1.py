class Account:
    def __init__(self, currency, owner_id):
        self.currency = currency
        self.owner_id = owner_id
        self.balance = 0
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Недостаточно средств")
        self.balance -= amount
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        self.balance += amount
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
        self.account[currency] = Account(currency, self.client_id)

    def close_account(self, currency):
        if currency  not in self.account:
            raise ValueError("Не удалось получть доступ к счёту")
        del self.account[currency]

    def get_account(self, currency):
        if currency not in self.account:
            raise ValueError("Не удалось получить доступ к счёту")
        return self.account[currency]

    def statement(self):
        lines = [f"Клиент: {self.name} (ID: {self.client_id})"]
        for acc in self.account.values():
            lines.append(f"Счёт в валюте {acc.currency}: {acc.balance}")
            return "\n".join(lines)

class BankAccount:
    def __init__(self):
        self.clients = {}
    def create_acc(self, client_id, name):
        if client_id not in self.clients:
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

bank = BankAccount()
