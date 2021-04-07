# Задание 19: Методы
# Создайте класс BankAccount с атрибутами:
# client_id, client_first_name, client_last_name, balance и методами add() и withdraw(),
# при помощи которых можно пополнять счет и выводить средства со счета соответственно.
# Атрибут balance должен инициализироваться по умолчанию значением 0.0,
# меняться при срабатывании методов add() и withdraw().

# class BankAccount:
#     def __init__(self, client_id, client_first_name, client_last_name, balance=0.0):
#         self.client_id = client_id
#         self.client_first_name = client_first_name
#         self.client_last_name = client_last_name
#         self.balance = balance
#
#     def add(self, money):
#         self.balance += money
#
#     def withdraw(self, money):
#         self.balance -= money
#
#
# new_client = BankAccount(1, 'Igor', 'Nikonov')
# print(new_client.balance)
# new_client.add(100)
# print(new_client.balance)
# new_client.withdraw(50)
# print(new_client.balance)
