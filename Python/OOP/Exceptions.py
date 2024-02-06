# Создайте класс BankAccount, который представляет банковский счет, у которого есть:
# метод __init__, принимающий баланс(атрибут balance)
# метод deposit для пополнения баланса. Если пользователь пытается внести отрицательную сумму на счет, должно возникать
# исключение NegativeDepositError("Нельзя пополнить счет отрицательным значением"):
# метод withdraw для вывода денег. Если пользователь пытается снять больше денег, чем есть на счете, должно возникать
# исключение InsufficientFundsError("Недостаточно средств для снятия")
# Исключения NegativeDepositError и InsufficientFundsError вам также необходимо создать

class NegativeDepositError(Exception):
    def __str__(self):
        return "Нельзя пополнить счет отрицательным значением"


class InsufficientFundsError(Exception):
    def __str__(self):
        return "Недостаточно средств для снятия"


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, val):
        if val < 0:
            raise NegativeDepositError
        self.balance += val

    def withdraw(self, val):
        if self.balance - val < 0:
            raise InsufficientFundsError
        self.balance -= val


# ----------------------------------------------------------------------------------------------------------------------

# (2)













