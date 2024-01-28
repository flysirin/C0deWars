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

# Класс Song должен содержать:
# метод __init__, который сохраняет в экземпляре два атрибута title и artist: название песни и исполнитель
# Класс Playlist должен содержать:
# метод __init__. , который создает в экземпляре атрибут songs. Изначально должен быть пустым списком;
# метод __getitem__ , который возвращает песню из атрибута songs по индексу
# метод __setitem__ , который добавляет песню в атрибут songs в указанный индекс. При этом нужно сдвинуть уже
# имеющиеся песни вправо, у которых индекс был до момента вставки равен или больше переданного
# метод add_song, который добавляет песню в конец плейлиста


# class Song:
#     def __init__(self, title, artist):
#         self.title = title
#         self.artist = artist
#
#
# class Playlist:
#     def __init__(self):
#         self.songs = []
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.songs):
#             return self.songs[item]
#
#     def __setitem__(self, key, value):
#         self.songs.insert(key, value)
#         # if 0 <= key < len(self.songs):
#         #     self.songs = self.songs[:key] + [value] + self.songs[key:]
#
#     def add_song(self, value):
#         self.songs.append(value)


# ----------------------------------------------------------------------------------------------------------------------

# (6)


# В этой задаче мы создадим аналог корзины покупок и для этого нам понадобиться реализовать класс ShoppingCart. В нем
# метод __init__. , который создает в экземпляре атрибут items. Изначально должен быть пустым словарем,
# в нем будут содержаться покупки;
# метод __getitem__ , который возвращает по названию товара его текущее количество или 0, если товар отсутствует в корзине
# метод __setitem__ , который проставляет по названию товара его количество в корзине. Если товар отсутствовал,
# его необходимо добавить, если присутствовал - нужно проставить ему новое количество
# метод __delitem__ , который удаляет товар из корзины
# метод add_item, который добавляет товар к текущим. Это значит, что если товар уже присутствовал в корзине,
# то необходимо увеличить его количество. Если товар отсутствовал, нужно его добавить. Данный метод принимает
# обязательно название товара и необязательно его количество (по умолчанию количество равно 1).
#  метод remove_item, который удаляет некоторое количество товара из корзины. Если хотят удалить из корзины
#  столько же товара, чем там имеется или больше, необходимо удалить его из корзины.
#  В остальных случаях уменьшаем количество товара на переденное количество.
#  Данный метод принимает обязательно название товара и необязательно его количество (по умолчанию количество равно 1).
#  Предусмотрите ситуацию, когда удаляемый товар отсутствует в корзине


# class ShoppingCart:
#     def __init__(self):
#         self.items = dict()
#
#     def __getitem__(self, item):
#         return self.items.get(item, 0)
#
#     def __setitem__(self, key, value):
#         self.items[key] = value
#
#     def __delitem__(self, key):
#         del self.items[key]
#
#     def add_item(self, key, value=1):
#         self.items[key] = self.items.get(key, 0) + value
#
#     def remove_item(self, key, value=1):
#         if self.items.get(key, 0):
#             if self.items[key] <= value:
#                 del self.items[key]
#             else:
#                 self.items[key] -= value


# ----------------------------------------------------------------------------------------------------------------------

# (7)


