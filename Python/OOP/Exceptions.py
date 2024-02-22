# Создайте класс BankAccount, который представляет банковский счет, у которого есть:
# метод __init__, принимающий баланс(атрибут balance)
# метод deposit для пополнения баланса. Если пользователь пытается внести отрицательную сумму на счет, должно возникать
# исключение NegativeDepositError("Нельзя пополнить счет отрицательным значением"):
# метод withdraw для вывода денег. Если пользователь пытается снять больше денег, чем есть на счете, должно возникать
# исключение InsufficientFundsError("Недостаточно средств для снятия")
# Исключения NegativeDepositError и InsufficientFundsError вам также необходимо создать

# class NegativeDepositError(Exception):
#     def __str__(self):
#         return "Нельзя пополнить счет отрицательным значением"
#
#
# class InsufficientFundsError(Exception):
#     def __str__(self):
#         return "Недостаточно средств для снятия"
#
#
# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance
#
#     def deposit(self, val):
#         if val < 0:
#             raise NegativeDepositError
#         self.balance += val
#
#     def withdraw(self, val):
#         if self.balance - val < 0:
#             raise InsufficientFundsError
#         self.balance -= val
#

# ----------------------------------------------------------------------------------------------------------------------

# (2)

# Для следующего задания нам нужно реализовать базовым класс исключения PasswordInvalidError, который наследуется от
# стандартного класса исключений Exception. Этот класс можно использовать для обработки любых общих ошибок, связанных с неверными паролями.
# От него нужно унаследовать следующие классы:
# PasswordLengthError представляет ошибку, связанную с недостаточной длиной пароля;
# PasswordContainUpperError представляет ошибку, связанную с отсутствием заглавных букв в пароле;
# PasswordContainDigitError представляет ошибку, связанную с отсутствием цифр в пароле.
# Создайте класс User с атрибутами username и password(пароль по умолчанию None). Класс должен иметь метод set_password,
# который принимает пароль и устанавливает его как значение атрибута password. Метод set_password должен также проверять,
# соответствует ли пароль заданным требованиям безопасности:
# Длина пароля должна быть не менее 8 символов (в противном случае генерируется исключение PasswordLengthError с
# текстом Пароль должен быть не менее 8 символов);
# Пароль должен содержать хотя бы одну заглавную букву (в противном случае генерируется исключение
# PasswordContainUpperError с текстом Пароль должен содержать хотя бы одну заглавную букву);
# Пароль должен содержать хотя бы одну цифру (в противном случае генерируется исключение PasswordContainDigitError
# с текстом Пароль должен содержать хотя бы одну цифру);


class PasswordInvalidError(Exception):
    pass

class PasswordLengthError(PasswordInvalidError):
    pass

class PasswordContainUpperError(PasswordInvalidError):
    pass

class PasswordContainDigitError(PasswordInvalidError):
    pass


class User:
    def __init__(self, username, password=None):
        self.username = username
        self.password = password

    def set_password(self, val):
        if len(val) < 8:
            raise PasswordLengthError("Пароль должен быть не менее 8 символов")
        if not any(map(lambda x: x.isupper(), val)):
            raise PasswordContainUpperError("Пароль должен содержать хотя бы одну заглавную букву")
        if not any(map(lambda x: x.isdigit(), val)):
            raise PasswordContainDigitError("Пароль должен содержать хотя бы одну цифру")

        self.password = val


assert issubclass(PasswordInvalidError, Exception)
assert issubclass(PasswordLengthError, PasswordInvalidError)
assert issubclass(PasswordContainUpperError, PasswordInvalidError)
assert issubclass(PasswordContainDigitError, PasswordInvalidError)

user = User("johndoe")

try:
    user.set_password("weakpwd")
except PasswordLengthError as e:
    print(e)

try:
    user.set_password("strongpassword8")
except PasswordContainUpperError as e:
    print(e)

try:
    user.set_password("Safepassword")
except PasswordContainDigitError as e:
    print(e)

user.set_password("SecurePass123")
assert user.password == 'SecurePass123'









