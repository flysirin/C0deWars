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


# class Card:
#     def __init__(self, rank, suit):
#         self.rank = rank
#         self.suit = suit
#
#     def __str__(self):
#         return f"{self.rank} {self.suit}"  # change
#
#
# class Deck:
#     ranks = [str(n) for n in range(2, 11)] + list('JQKA')
#     suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
#
#     def __init__(self):
#         self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
#         self.inx = 0
#
#     def __iter__(self):             # change
#         return iter(self.cards)
#
#     # def __next__(self):
#     #     if self.inx >= len(self.cards):
#     #         raise StopIteration
#     #     self.inx += 1
#     #     return f"{self.cards[self.inx - 1].rank} {self.cards[self.inx - 1].suit}"
#
#
# deck = Deck()
# for card in deck:
#     print(card)


# ----------------------------------------------------------------------------------------------------------------------

# (8)
# Ниже в коде представлена реализация класса FileReader, который должен при итерирации считывать построчно содержимое файла
# Ваша задача дописать метод __next__, чтобы он возвращал по порядку строки из файла, пока содержимое файла не закончится. Строку нужно очистить слева и справа от символов пробелов и переносов на новую строку


# class FileReader:
#     def __init__(self, filename):
#         self.file = open(filename)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         # new_line = self.file.readline()
#         # while new_line:
#         #     return new_line.strip()
#         # self.file.close()
#         # raise StopIteration
#
#         return next(self.file).strip()  # by default file open in text mode
#
#
# for line in FileReader('lorem.txt'):
#     print(line)


# ----------------------------------------------------------------------------------------------------------------------

# (9)

# Нужно создать итератор SequenceIterator, который принимает контейнер данных в виде списка в момент инициализации и сохраняет его в атрибуте ЭК
# SequenceIterable([1, 5, 4, 6, 43, True, 'hello'])
# При итерации объект SequenceIterator должен  сперва выдать все элементы, находящиеся на четных индексах
# (0, 2, 4 и т.д), а затем элементы, имеющие нечетные индексы (1, 3, 5 и т.д.)


# class SequenceIterator:
#     def __init__(self, container):
#         self.container = container
#         self.indexes = iter(tuple(range(0, len(self.container), 2)) + tuple(range(1, len(self.container), 2)))
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         return self.container[next(self.indexes)]

###

# class SequenceIterator:
#     def __init__(self, args):
#         self.args = args
#
#     def __iter__(self):
#         even = self.args[::2]
#         odd = self.args[1::2]
#         return iter(even + odd)
#
# container = SequenceIterator([1, 5, 4, 6, 43, True, 'hello'])
# for i in container:
#     print(i)
# # # Печатает
# # 1
# # 4
# # 43
# # hello
# # 5
# # 6
# # True


# ----------------------------------------------------------------------------------------------------------------------

# (10)

# У вас имеется готовый код класса Stack (см. ниже в блоке кода). Обратите внимание на реализацию метода __iter__
# def __iter__(self):
#     return StackIterator(self)
# Значит класс Stack логику перебора элементов делегирует классу StackIterator. Ваша задача реализовать итератор в
# классе StackIterator, который обходит элементы стека сверху вниз
# Необходимо написать только реализацию класса StackIterator

# class StackIterator:
#     def __init__(self, stack):
#         self.stack = stack
#         self.idx = len(self.stack.items)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.idx <= 0:
#             raise StopIteration
#         self.idx -= 1
#         return self.stack.items[self.idx]
#
#
# class Stack:
#     def __init__(self):
#         self.items = []
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         if len(self.items) == 0:
#             print("Empty Stack")
#         else:
#             return self.items.pop()
#
#     def peek(self):
#         if len(self.items) == 0:
#             print("Empty Stack")
#         else:
#             return self.items[-1]
#
#     def is_empty(self):
#         return len(self.items) == 0
#
#     def size(self):
#         return len(self.items)
#
#     def __iter__(self):
#         return StackIterator(self)
#
#
# stack = Stack()
#
# stack.push(100)
# stack.push(True)
# stack.push('hello')
# stack.push('world')
#
# # Используем итератор для обхода стека
# for item in stack:
#     print(item)
#
# # world
# # hello
# # True
# # 100


# ----------------------------------------------------------------------------------------------------------------------

# (11)


# Создайте объект итератор FibonacciIterator, который умеет выдавать последовательность Фибоначчи из n чисел.
# Число n поступает при инициализации класса FibonacciIterator.
# Будем считать, что последовательность Фибиначчи следующая: 0, 1, 1, 2, 3, 5, 8, 13, 21 и т.д.
# Каждое следующее число получается суммой двух предыдущих.


# class FibonacciIterator:
#     def __init__(self, limit):
#         self.limit = limit
#         self.counter = 0
#         self.a, self.b = 0, 1
#
#     def __next__(self):
#         if self.counter >= self.limit:
#             raise StopIteration
#         self.b += self.a
#         self.b, self.a = self.a, self.b
#         self.counter += 1
#         return self.b
#
#     def __iter__(self):
#         return self
#
#
# fibonacci_iter = FibonacciIterator(7)
# for number in fibonacci_iter:
#     print(number)


# ----------------------------------------------------------------------------------------------------------------------

# (12)

# Представьте, у ,библиотекаря имеется огромная коллекция книг. В какую-то из этих книг он в далекой молодости
# положил 666 песо и теперь хочет их отыскать. Его внук начал изучать python  и познакомился с концепцией итератора.
# Предложил обойти все книги по порядку добавления их в библиотеку, и затем для каждой отдельной книги обойти все
# ее страницы. Но сам это реализовать не смог, просит помочь именно вас.
# От внука вам досталась реализация классов Book и Library. Класс Library делегирует реализацию итератора
# классу LibraryIterator
# def __iter__(self):
#     return LibraryIterator(...)
# Вот здесь у внука библиотекаря и возникла проблема. Он не знает, что передавать в LibraryIterator и организовать
# обход этой коллекции. Помогите внучку, ведь ему еще математику делать на завтра.
# Необходимо написать только реализацию класса LibraryIterator, который обходит элементы библиотеки согласно примеру,
# расположенному в коде ниже. Изучите код проверки класса LibraryIterator и ожидаемый вывод


# class Book:
#     def __init__(self, title, pages):
#         self.title = title
#         self.pages = pages
#
#
# class Library:
#     def __init__(self):
#         self.books = []
#
#     def add_book(self, book):
#         self.books.append(book)
#
#     def __iter__(self):
#         return LibraryIterator(self)  # тут определите, что будете передавать итератору
#
#
# class LibraryIterator:
#     def __init__(self, lib: Library):
#         self.lib = lib
#         self.pages = iter([page for books in self.lib.books for page in books.pages])
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         return next(self.pages)
#
#
#
# # Пример использования
# book1 = Book("Book 1", ["Page 1", "Page 2", "Page 3", "Page 4"])
# book2 = Book("Book 2", ["Page A", "Page B", "Page C"])
# book3 = Book("Book 3", ["Chapter 1", "Chapter 2"])
#
# library = Library()
# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)
#
# # Используем вложенный итератор для обхода страниц в библиотеке
# for page in library:
#     print(page)


# ----------------------------------------------------------------------------------------------------------------------

# (13)


# Создайте класс InfinityIterator, который реализует бесконечный итератор. Он должен возвращать элементы
# арифметической прогрессии с шагом 10. Начальное значение арифметическое прогрессии по умолчанию равно 0,
# но может быть передано при инициализации класса InfinityIterator.
# Каждый член арифметической прогрессии равен предыдущему, сложенному с одним и тем же числом d.
# В нашем случае значение d=10.


# class InfinityIterator:
#     def __init__(self, num=0):
#         self.num = num
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         curr_num = self.num
#         self.num += 10
#         return curr_num


# ----------------------------------------------------------------------------------------------------------------------

# (14)

# Создайте класс AttributeChecker, который имеет:
# магический метод __contains__, принимающий имя атрибута и возвращает True, если этот атрибут существует в экземпляре
# класса, и False в противном случае.

class AttributeChecker:
    def __contains__(self, item):
        if item in self.__dict__:
            return True
        return False








