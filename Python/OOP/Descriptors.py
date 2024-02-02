# ----------------------------------------------------------------------------------------------------------------------

# (1)

# class CoordinateValue:
#     def __set__(self, instance, value):
#         print(f'__set__ called, instance={instance}, value={value}')
#
#     def __get__(self, instance, owner_class):
#         if instance is None:
#             print('__get__ called from class')
#         else:
#             print(f'__get__ called, instance={instance}, owner_class={owner_class}')
#
#
# class Point:
#     x = CoordinateValue()
#     y = CoordinateValue()
#
#
# Point.x
# p = Point()
# p.x
# p.x = 100
#

# ----------------------------------------------------------------------------------------------------------------------

# (2)

# Создайте дескриптор MaxLengthAttribute, который возвращает имя самого длинного атрибута в экземпляре.
# Если несколько атрибутов имеют одинаковую длину, необходимо вернуть значение, стоящее последним по лексикографическому порядку без учета регистра букв.
# Если у экземпляра отсутствуют свои собственные атрибуты, необходимо вернуть None.
# Ваша задача написать только определение класса MaxLengthAttribute


# class MaxLengthAttribute:
#     def __get__(self, instance, owner):
#         if instance.__dict__:
#             return max(instance.__dict__.keys(), key=len)
#
#
# class JustClass:
#     max_atr = MaxLengthAttribute()
#
#
# obj = JustClass()
# obj.name = "Vasiliy"
# obj.city = "Saint Peterburg"
# obj.mock = 15
# obj.door = 'wood'
#
# print(obj.max_atr)

# ----------------------------------------------------------------------------------------------------------------------

# (3)

# Создайте дескриптор RangeValidator, который валидирует значение на принадлежность к определенному интервалу.
# При инициализации класс RangeValidator получает значение начала и конца интервала.
# При попытке сохранить нечисловое значение в дескриптор, необходимо вызывать исключение :
# TypeError('Неправильный тип данных')
# При попытке сохранить значение в дескриптор, которое не принадлежит интервалу, необходимо вызывать исключение:
# ValueError(f"Значение должно быть между <начало_интервала> и <конец_интервала>")
# Ваша задача реализовать только класс RangeValidator


# class RangeValidator:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#
#     def __set_name__(self, owner, name):
#         self._name = '_' + name
#
#     def __set__(self, instance, value):
#         if type(value) not in (int, float):
#             raise TypeError('Неправильный тип данных')
#         if not self.start <= value <= self.end:
#             raise ValueError(f"Значение должно быть между {self.start} и {self.end}")
#         setattr(instance, self._name, value)


# ----------------------------------------------------------------------------------------------------------------------

# (4)

# проверять не только минимальную, но и на максимальную возможную длину строки. Если символов больше, чем должно быть, необходимо вызвать исключение
# ValueError("Длина атрибута <attribute_name> должна быть не больше <max_length> символов")
# проверять на наличие недопустимых символов. Если хотя бы один такой символ встречается в строке, необходимо вызвать исключение
# ValueError("Имеются недопустимые символы в атрибуте <название атрибута>")
# проверять, что все символы имеют одинаковый регистр (все только заглавные или только все строчные). Если проверка не выполняется, необходимо вызвать исключение
# ValueError("Все буквы должны быть в одном регистре в атрибуте <название атрибута>")
# Перечисленные проверки являются необязательными. Их необходимо выполнять, только если будут переданы значения в соответствующие атрибуты:
# min_length принимает числовое значение, которое ставит условие на минимальную допустимую длину. По умолчанию None
# max_length принимает числовое значение, которое ставит условие на максимальную допустимую длину. По умолчанию None
# exclude_chars принимает строковое значение, символы которого недопустимы в новом значении. По умолчанию None
# is_same_register принимает булево значение. По умолчанию False. Если будет передано значение True, необходимо выполнять проверку на регистр букв.


# class StringValidation:
#     def __init__(self, min_length=None, max_length=None, exclude_chars=None, is_same_register=False):
#         self.min_length = min_length
#         self.max_length = max_length
#         self.exclude_chars = exclude_chars
#         self.is_same_register = is_same_register
#
#     def __set_name__(self, owner_class, attribute_name):
#         self.attribute_name = attribute_name
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f'В атрибут {self.attribute_name} можно сохранять только строки')
#         if self.min_length and len(value) < self.min_length:
#             raise ValueError(f'Длина атрибута {self.attribute_name} должна '
#                              f'быть не меньше {self.min_length} символов')
#         if self.max_length and len(value) > self.max_length:
#             raise ValueError(f'Длина атрибута {self.attribute_name} должна '
#                              f'быть не больше {self.max_length} символов')
#         if self.exclude_chars and set(value).intersection(set(self.exclude_chars)):
#             raise ValueError(f"Имеются недопустимые символы в атрибуте {self.attribute_name}")
#         if self.is_same_register and not self.check_register(value):
#             raise ValueError(f"Все буквы должны быть в одном регистре в атрибуте {self.attribute_name}")
#
#         instance.__dict__[self.attribute_name] = value
#
#     def __get__(self, instance, owner_class):
#         if instance is None:
#             return self
#         else:
#             print(f'calling __get__ for {self.attribute_name}')
#             return instance.__dict__.get(self.attribute_name, None)
#
#     @staticmethod
#     def check_register(value: str):
#         return value.islower() or value.isupper()
#
#
# class Person:
#     name = StringValidation(is_same_register=True, exclude_chars='tyur')
#     last_name = StringValidation(max_length=10, is_same_register=True)
#
#
# p = Person()
# try:
#     p.name = 'Michail Second'
# except ValueError as ex:
#     print(ex)
# try:
#     p.last_name = 'LERMONTOV'
# except ValueError as ex:
#     print(ex)
# print(p.name, p.last_name)

# ----------------------------------------------------------------------------------------------------------------------

# (5)

















# ----------------------------------------------------------------------------------------------------------------------

# (6)

# ----------------------------------------------------------------------------------------------------------------------

# (7)
