# (1)
# class Hero:
#     def __len__(self):
#         return len(self.__dict__)
#
#     def __str__(self):
#         return "\n".join(f"{k}: {v}" for k, v in sorted(self.__dict__.items()))

# ----------------------------------------------------------------------------------------------------------------------

# (2)
# Создайте класс  Order, который имеет следующие методы:
# метод __init__, который устанавливает значения атрибутов cart и customer: список покупок и имя покупателя
# магический метод __add__, который описывает добавления товара в список покупок. Результатом такого сложения должен
# быть новый заказ, в котором все покупки берутся из старого заказа и в конец добавляется новый товар.
# Покупатель в заказе остается прежним
# магический метод __radd__, который описывает добавления товара в список покупок при правостороннем сложении.
# Результатом такого сложения должен быть новый заказ, в котором все покупки берутся из старого заказа и в начало списка
# покупок добавляется новый товар. Покупатель в заказе остается прежним
#  магический метод __sub__, который описывает исключение товара из списка покупок. Результатом вычитания должен быть новый заказ
# магический метод __rsub__, который описывает исключение товара из списка покупок при правостороннем вычитании.
# Результатом должен быть таким же как и при __sub__

#
# class Order:
#     def __init__(self, cart: list,  customer: str):
#         self.cart = cart
#         self.customer = customer
#
#     def __add__(self, other):
#         return Order(self.cart + [other], self.customer)
#
#     def __radd__(self, other):
#         return Order([other] + self.cart, self.customer)
#
#     def __sub__(self, other):
#         if other in self.cart:
#             self.cart.remove(other)
#         return Order(self.cart, self.customer)
#
#     def __rsub__(self, other):
#         if other in self.cart:
#             self.cart.remove(other)
#         return Order(self.cart, self.customer)

# ----------------------------------------------------------------------------------------------------------------------

# (3)
# Декоратор класса @total_ordering из модуля functools позволяет определить в классе лишь метод __eq__() и один из
# методов __lt__(), __le__(), __gt__() или __ge__(). Все недостающие методы декоратор определит и реализует самостоятельно.
# Создайте класс  Rectangle, который имеет:
# метод __init__, который устанавливает значения атрибутов width и height: ширина и высота прямоугольника
# свойство area, возвращающее площадь прямоугольника
# методы сравнения. Здесь вы сами решаете какие магические методы реализовывать, главное чтобы прямоугольники
# могли сравниваться с числами и между собой по значению площади. Используйте декоратор @total_ordering

# from functools import total_ordering
#
#
# @total_ordering
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     @property
#     def area(self):
#         return self.height * self.width
#
#     def __eq__(self, other):
#         if isinstance(other, (int, float)):
#             return self.area == other
#         return self.area == other.area
#
#     def __lt__(self, other):
#         if isinstance(other, (int, float)):
#             return self.area < other
#         return self.area < other.area


# ----------------------------------------------------------------------------------------------------------------------

# (4)

# Ваша задача дописать классы BankAccount и Numbers таким образом, чтобы их экземпляры могли участвовать в операции
# сложения с числами и c другими экземплярами классов BankAccount и Numbers


# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#
#     def __str__(self):
#         return self.name
#
#     def __add__(self, other):
#         if isinstance(other, (int, float)):
#             return self.balance + other
#         if isinstance(other, (BankAccount, Numbers)):
#             return self.balance + other.balance
#
#     def __radd__(self, other):
#         return self + other
#
#
# class Numbers:
#     def __init__(self, values: list):
#         self._values = values
#
#     @property
#     def balance(self):
#         return sum(self._values)
#
#     def __add__(self, other):
#         if isinstance(other, (int, float)):
#             return self.balance + other
#         if isinstance(other, (BankAccount, Numbers)):
#             return self.balance + other.balance
#
#     def __radd__(self, other):
#         return self + other

# ----------------------------------------------------------------------------------------------------------------------

# (5)





