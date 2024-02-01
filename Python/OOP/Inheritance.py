# Если value отсутствует в списке, происходит исключение ValueError.
# Ваша задача создать метод .remove_all(value), который будет удалять сразу все значения, которые равны value.
# Если value отсутствует в списке, ничего делать не нужно. Метод в конце своей работы должен вернуть None

#
# class MyList(list):
#     def remove_all(self, value):
#         while value in self:
#             self.remove(value)


# ----------------------------------------------------------------------------------------------------------------------

# (2)

# class BasePizza:
#     BASE_PIZZA_PRICE = 15
#
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#         self.toppings = ['cheese']
#
#     def __str__(self):
#         return f"{self.name} with {self.toppings}, ${self.price:.2f}"
#
#
# class PepperoniMixin:
#     def add_pepperoni(self):
#         print("Adding pepperoni!")
#         self.price += 5
#         self.toppings += ['pepperoni']
#
#
# class MushroomMixin:
#     def add_mushrooms(self):
#         print("Adding mushrooms!")
#         self.price += 3
#         self.toppings += ['mushrooms']
#
#
# class OnionMixin:
#     def add_onion(self):
#         print("Adding onion!")
#         self.price += 2
#         self.toppings += ['onion']
#
#
# class BaconMixin:
#     def add_bacon(self):
#         print("Adding bacon!")
#         self.price += 6
#         self.toppings += ['bacon']
#
#
# class OlivesMixin:
#     def add_olives(self):
#         print("Adding olives!")
#         self.price += 1
#         self.toppings += ['olives']
#
#
# class HamMixin:
#     def add_ham(self):
#         print("Adding ham!")
#         self.price += 7
#         self.toppings += ['ham']
#
#
# class PepperMixin:
#     def add_pepper(self):
#         print("Adding pepper!")
#         self.price += 3
#         self.toppings += ['pepper']
#
#
# class ChickenMixin:
#     def add_chicken(self):
#         print("Adding chicken!")
#         self.price += 5
#         self.toppings += ['chicken']
#
#
# class OlivesPizza(BasePizza, OlivesMixin):
#
#     def __init__(self):
#         super().__init__('Море оливок', BasePizza.BASE_PIZZA_PRICE)
#         self.add_olives()
#
#
# class PepperoniPizza(BasePizza, PepperoniMixin):
#
#     def __init__(self):
#         super().__init__('Колбасятина', BasePizza.BASE_PIZZA_PRICE)
#         self.add_pepperoni()
#
#
# class MushroomOnionBaconPizza(BasePizza, MushroomMixin, OnionMixin, BaconMixin):
#
#     def __init__(self):
#         super().__init__('Грибной пяточок с луком', BasePizza.BASE_PIZZA_PRICE)
#         self.add_mushrooms()
#         self.add_onion()
#         self.add_bacon()
#
#
# # Создайте экземпляр CountryPizza в переменной pizza
#
# class CountryPizza(BasePizza, HamMixin, PepperMixin, OlivesMixin,PepperoniMixin, MushroomMixin, ChickenMixin):
#     def __init__(self):
#         super().__init__('Деревенская пицца', BasePizza.BASE_PIZZA_PRICE)
#         self.add_ham()
#         self.add_pepper()
#         self.add_olives()
#         self.add_pepperoni()
#         self.add_mushrooms()
#         self.add_chicken()
#
#
# pizza = CountryPizza()
#
#
# # Код для проверки
#
# assert pizza.name == 'Деревенская пицца'
# assert pizza.price == 39
# assert pizza.toppings == ['cheese', 'ham', 'pepper', 'olives', 'pepperoni', 'mushrooms', 'chicken']
# print(pizza)

# ----------------------------------------------------------------------------------------------------------------------

# (3)



# Создайте класс PermissionMixin, который будет иметь следующие методы:
# __init__(self): метод инициализации, который создает множество permissions для хранения разрешений.
# В него мы будем сохранять действия, которые будут доступны пользователям, например Чтение, Запись, Выполнение и т.д.
# grant_permission(self, permission): метод для назначения разрешения. Добавляет переданное разрешение
# в множество permissions
# revoke_permission(self, permission): метод для отмены разрешения. Удаляет переданное разрешение из множества permissions
# has_permission(self, permission): метод для проверки наличия разрешения. Возвращает True,
# если переданное разрешение присутствует в множестве permissions, и False в противном случае.
# Создайте класс User, который будет наследоваться от PermissionMixin и иметь следующие атрибуты:
# name: имя пользователя.
# email: email пользователя.

# class PermissionMixin:
#     def __init__(self):
#         self.permissions = set()
#
#     def grant_permission(self, permission):
#         self.permissions.add(permission)
#
#     def revoke_permission(self, permission):
#         self.permissions.discard(permission)
#
#     def has_permission(self, permission):
#         return permission in self.permissions
#
#
# class User(PermissionMixin):
#     def __init__(self, name, email):
#         super(User, self).__init__()
#         self.name = name
#         self.email = email
#
#
# user1 = User('Alice', 'alice@example.com')
# user2 = User('Bob', 'bob@example.com')
#
# assert user1.email == 'alice@example.com'
# assert user1.name == 'Alice'
# assert user1.permissions == set()
#
# assert user2.email == 'bob@example.com'
# assert user2.name == 'Bob'
# assert user2.permissions == set()
#
# user1.grant_permission('read')
# user1.grant_permission('write')
# user2.grant_permission('read')
# assert user1.permissions == {'read', 'write'}
# assert user2.permissions == {'read'}
#
# assert user1.has_permission('read') is True
# assert user1.has_permission('write') is True
# assert user1.has_permission('execute') is False
#
# assert user2.has_permission('read') is True
# assert user2.has_permission('write') is False
# assert user2.has_permission('execute') is False
#
# user1.revoke_permission('write')
# user1.revoke_permission('execute')
#
# assert user1.has_permission('read') is True
# assert user1.has_permission('write') is False
# assert user1.has_permission('execute') is False
#
# print('Good')


# ----------------------------------------------------------------------------------------------------------------------

# (4)














