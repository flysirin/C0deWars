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
# Класс DictMixin представляет собой миксин, который добавляет в класс, наследующий его, метод to_dict().
# Этот метод позволяет преобразовать объект в словарь.
# Внутри класса DictMixin вы можете создавать сколько угодно служебных методов и атрибутов, которые помогут
# вам справиться с задачей. Главное, это реализовать метод to_dict(), он являться точкой входа для взаимодействия с
# вашим миксином и он должен вернуть представление вашего объекта в виде словаря. Обратите внимание на вложенность атрибутов.


# class DictMixin:
#     excludes_types = (int, float, str)
#
#     def to_dict(self):
#         return eval(self.__repr__())
#
#     def __repr__(self):
#         return str(self.__dict__)
#

####

# import json
#
# class DictMixin:
#
#     def to_dict(self):
#         a = json.dumps(self.__dict__, indent=2, default=lambda x: x.__dict__)
#         s = json.loads(a)
#         return s

####

#
# class Phone(DictMixin):
#     def __init__(self, number):
#         self.number = number
#
#
# class Person(DictMixin):
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
#
#
# class Address(DictMixin):
#     def __init__(self, street, city, state, zip_code):
#         self.street = street
#         self.city = city
#         self.state = state
#         self.zip_code = zip_code
#
#
# class Company(DictMixin):
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address
#
#
# address = Address("123 Main St", "Anytown", "CA", "12345")
# john_doe = Person("John Doe", 30, address)
#
# john_doe_dict = john_doe.to_dict()
# print(john_doe_dict)
# print(type(john_doe_dict))
#
#
# assert john_doe_dict == {'name': 'John Doe', 'age': 30, 'address': {'street': '123 Main St', 'city': 'Anytown', 'state': 'CA', 'zip_code': '12345'}}
#
# address = Address("123 Main St", "Albuquerque", "NM", "987654")
# assert address.to_dict() == {
#     'street': '123 Main St',
#     'city': 'Albuquerque',
#     'state': 'NM',
#     'zip_code': '987654'
# }
# walter = Person("Walter White", 30, address)
# assert walter.to_dict() == {'address': {'city': 'Albuquerque',
#                                         'state': 'NM',
#                                         'street': '123 Main St',
#                                         'zip_code': '987654'},
#                             'age': 30,
#                             'name': 'Walter White'}
#
# walter_phone = Phone("555-1234")
# walter.phone = walter_phone
# assert walter.to_dict() == {'address': {'city': 'Albuquerque',
#                                         'state': 'NM',
#                                         'street': '123 Main St',
#                                         'zip_code': '987654'},
#                             'age': 30,
#                             'name': 'Walter White',
#                             'phone': {'number': '555-1234'}}
#
# company_address = Address("3828 Piermont Dr", "Albuquerque", "NM", "12345")
# company = Company("SCHOOL", company_address)
#
# assert company.to_dict() == {'address': {'city': 'Albuquerque',
#                                          'state': 'NM',
#                                          'street': '3828 Piermont Dr',
#                                          'zip_code': '12345'},
#                              'name': 'SCHOOL'}
#
# jesse_address = Address("456 Oak St", "Albuquerque", "NM", "12345")
# jesse = Person("Jesse Bruce Pinkman", 27, jesse_address)
# jesse.phone = Phone("555-5678")
#
# fring = Person("Gustavo Fring", 55, Address("Los Pollos Hermanos", "Albuquerque", "NM", "12345"))
# fring.friends = [walter, jesse]
# print(fring.to_dict())
# assert fring.to_dict() == {'address': {'city': 'Albuquerque',
#                                        'state': 'NM',
#                                        'street': 'Los Pollos Hermanos',
#                                        'zip_code': '12345'},
#                            'age': 55,
#                            'friends': [{'address': {'city': 'Albuquerque',
#                                                     'state': 'NM',
#                                                     'street': '123 Main St',
#                                                     'zip_code': '987654'},
#                                         'age': 30,
#                                         'name': 'Walter White',
#                                         'phone': {'number': '555-1234'}},
#                                        {'address': {'city': 'Albuquerque',
#                                                     'state': 'NM',
#                                                     'street': '456 Oak St',
#                                                     'zip_code': '12345'},
#                                         'age': 27,
#                                         'name': 'Jesse Bruce Pinkman',
#                                         'phone': {'number': '555-5678'}}],
#                            'name': 'Gustavo Fring'}
#
# print('Good')

# ----------------------------------------------------------------------------------------------------------------------

# (5)

# Теперь давайте выполним сериализацию объектов, атрибутами которых могут быть другие объекты. Для этого переделайте
# миксин JsonSerializableMixin, так чтобы он мог сериализовать такие объекты.
# Внутри миксина JsonSerializableMixin обязательно должен быть метод to_json(), который возвращает итоговую строку
# сериализации объекта. Все остальное вы можете создавать по своему усмотрению

# import json
#
#
# class JsonSerializableMixin:
#     def to_json(self):
#         return json.dumps(self.__dict__, default=lambda x: x.__dict__)
#
#
# class Person(JsonSerializableMixin):
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
#
#
# class Address(JsonSerializableMixin):
#     def __init__(self, street, city, state, zip_code):
#         self.street = street
#         self.city = city
#         self.state = state
#         self.zip_code = zip_code
#
#
# class Company(JsonSerializableMixin):
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address
#
#
# address = Address("123 Main St", "Albuquerque", "NM", "987654")
# print(address.to_json())
# assert address.to_json() == '{"street": "123 Main St", "city": "Albuquerque", "state": "NM", "zip_code": "987654"}'
#
# walter = Person("Walter White", 30, address)
# walter.hobby = ['Chemistry', 'Cooking']
# walter.is_danger = True
#
# company_address = Address("3828 Piermont Dr", "Albuquerque", "NM", "12345")
# walter.company = Company("SCHOOL", company_address)
# assert walter.to_json() == '{"name": "Walter White", "age": 30, "address": {"street": "123 Main St", "city": "Albuquerque", "state": "NM", "zip_code": "987654"}, "hobby": ["Chemistry", "Cooking"], "is_danger": true, "company": {"name": "SCHOOL", "address": {"street": "3828 Piermont Dr", "city": "Albuquerque", "state": "NM", "zip_code": "12345"}}}'
#
# jesse_address = Address("456 Oak St", "Albuquerque", "NM", "12345")
# jesse = Person("Jesse Bruce Pinkman", 27, jesse_address)
# walter.is_lucky = False
#
# fring = Person("Gustavo Fring", 55, Address("Los Pollos Hermanos", "Albuquerque", "NM", "12345"))
# fring.friends = [walter, jesse]
#
# assert fring.to_json() == '{"name": "Gustavo Fring", "age": 55, "address": {"street": "Los Pollos Hermanos", "city": "Albuquerque", "state": "NM", "zip_code": "12345"}, "friends": [{"name": "Walter White", "age": 30, "address": {"street": "123 Main St", "city": "Albuquerque", "state": "NM", "zip_code": "987654"}, "hobby": ["Chemistry", "Cooking"], "is_danger": true, "company": {"name": "SCHOOL", "address": {"street": "3828 Piermont Dr", "city": "Albuquerque", "state": "NM", "zip_code": "12345"}}, "is_lucky": false}, {"name": "Jesse Bruce Pinkman", "age": 27, "address": {"street": "456 Oak St", "city": "Albuquerque", "state": "NM", "zip_code": "12345"}}]}'
# print('Good')


# ----------------------------------------------------------------------------------------------------------------------

# (6)


# Создайте класс с именем Person, экземпляры которого имеют следующие атрибуты:
# first_name хранит имя человека в виде строки;
# last_name строка, хранит фамилию человека в виде строки;
# age хранит возраст человека в виде целого числа.
# Переопределите также метод __str__ так, чтобы он возвращал строку
# {Имя} {Фамилия} is {Возраст} years old
# Используйте атрибут __slots__ для указания атрибутов, чтобы каждый экземпляр класса использовал только память,
# необходимую для хранения перечисленных атрибутов.


# class Person:
#     __slots__ = ['first_name', 'last_name', 'age']
#
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name} is {self.age} years old"


# ----------------------------------------------------------------------------------------------------------------------

# (7)

# Создайте класс Device, который будет служить базовым классом для всех устройств в доме. Класс "Device" должен иметь
# "slots" для защищенных атрибутов "_name", "_location" и "_status"(по умолчанию ON). Для атрибут "_name" создайте
# свойство только для чтения, а для атрибутов "_location" и "_status" - свойства для чтения и записи. Добавьте метод
# "turn_on" для изменения статуса устройства на "ON" и метод "turn_off" для изменения статуса на "OFF".
# Создайте класс Light, который будет наследоваться от класса "Device" и представлять устройства освещения. Для этого
# определите слоты для атрибутов "_brightness" и "_color". Для атрибута "_brightness" создайте свойство для чтения и
# записи, а для атрибута "_color" - только для чтения.
# Создайте класс Thermostat, который будет наследоваться от класса "Device" и представлять устройства управления
# температурой. В классе Thermostat определите слоты для атрибутов "_current_temperature" и "_target_temperature".
# Оба атрибута должны управляться свойствами для чтения и записи.
# Создайте класс SmartTV, который будет наследоваться от класса "Device" и представлять устройства для просмотра
# телевизионных каналов. В классе SmartTV определите слоты для атрибута "_channel". Создайте свойства для управления
# чтением и записью атрибута _channel.

# class Device:
#     __slots__ = '_name', '_location', '_status'
#
#     def __init__(self, name, location):
#         self._name = name
#         self._location = location
#         self._status = 'ON'
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def location(self):
#         return self._location
#
#     @location.setter
#     def location(self, value):
#         self._location = value
#
#     @property
#     def status(self):
#         return self._status
#
#     @status.setter
#     def status(self, value):
#         self._status = value
#
#     def turn_on(self):
#         self._status = 'ON'
#
#     def turn_off(self):
#         self._status = 'OFF'
#
#
# class Light(Device):
#     __slots__ = "_brightness", "_color"
#
#     def __init__(self, name, location,   brightness, color):
#         super().__init__(name, location)
#         self._brightness = brightness
#         self._color = color
#
#     @property
#     def brightness(self):
#         return self._brightness
#
#     @brightness.setter
#     def brightness(self, value):
#         self._brightness = value
#
#     @property
#     def color(self):
#         return self._color
#
#
# class Thermostat(Device):
#     __slots__ = "_current_temperature", "_target_temperature"
#
#     def __init__(self, name, location, temp, targ_temp):
#         super().__init__(name, location)
#         self._current_temperature = temp
#         self._target_temperature = targ_temp
#
#     @property
#     def current_temperature(self):
#         return self._current_temperature
#
#     @current_temperature.setter
#     def current_temperature(self, value):
#         self._current_temperature = value
#
#     @property
#     def target_temperature(self):
#         return self._target_temperature
#
#     @target_temperature.setter
#     def target_temperature(self, value):
#         self._target_temperature = value
#
#
# class SmartTV(Device):
#     __slots__ = "_channel"
#
#     def __init__(self, name, location, channel):
#         super().__init__(name, location)
#         self._channel = channel
#
#     @property
#     def channel(self):
#         return self._channel
#
#     @channel.setter
#     def channel(self, value):
#         self._channel = value
#

# ----------------------------------------------------------------------------------------------------------------------

# (8)

# Создайте абстрактный класс Employee, имеющий абстрактный метод calculate_salary().
# Реализуйте два класса HourlyEmployee и SalariedEmployee, унаследованные от Employee, реализующие метод calculate_salary() для расчета заработной платы по часам и окладу соответственно.
# Класс HourlyEmployee при инициализации должен создавать атрибуты hours_worked и hourly_rate.
# Класс SalariedEmployee при инициализации должен создавать только атрибут monthly_salary.

# from abc import ABC, abstractmethod
#
#
# class Employee(ABC):
#
#     @abstractmethod
#     def calculate_salary(self):
#         pass
#
#
# class HourlyEmployee(Employee):
#     def __init__(self, hour, rate):
#         self.hours_worked = hour
#         self.hourly_rate = rate
#
#     def calculate_salary(self):
#         return self.hours_worked * self.hourly_rate
#
#
# class SalariedEmployee(Employee):
#     def __init__(self, monthly_salary):
#         self.monthly_salary = monthly_salary
#
#     def calculate_salary(self):
#         return self.monthly_salary


# ----------------------------------------------------------------------------------------------------------------------

# (9)


# Создайте абстрактный класс Database, в котором имеются следующие абстрактные методы:
# connect
# disconnect
# execute
# Создайте классы MySQLDatabase и PostgreSQLDatabase, которые будут наследовать абстрактный класс Database и реализовывать его абстрактные методы. В каждом классе, должны быть реализованы метод connect для подключения к соответствующей базе данных и метод disconnect для отключения от базы данных, также метод execute, который должен выполнять запрос на соответствующей базе данных.
# Внутри класса MySQLDatabase:
# Метод connect должен печатать на экран сообщение Connecting to MySQL database...
# Метод  disconnect должен печатать на экран сообщение Disconnecting from MySQL database...
# Метод  execute должен принимать запрос к базе данных в виде строки и печатать на экран сообщение Executing query '{query}' in MySQL database...
# Внутри класса PostgreSQLDatabase:
# Метод connect должен печатать на экран сообщение Connecting to PostgreSQL database...
# Метод  disconnect должен печатать на экран сообщение Disconnecting from PostgreSQL database...
# Метод  execute должен принимать запрос к базе данных в виде строки и печатать на экран сообщение Executing query '{query}' in PostgreSQL database...

# from abc import  ABC, abstractmethod
#
# class Database(ABC):
#     @abstractmethod
#     def connect(self):
#         pass
#
#     @abstractmethod
#     def disconnect(self):
#         pass
#
#     @abstractmethod
#     def execute(self, query):
#         pass
#
#
# class MySQLDatabase(Database):
#     def connect(self):
#         print('Connecting to MySQL database...')
#
#     def disconnect(self):
#         print('Disconnecting from MySQL database...')
#
#     def execute(self, query):
#         print(f"Executing query '{query}' in MySQL database...")
#
#
# class PostgreSQLDatabase(Database):
#     def connect(self):
#         print('Connecting to PostgreSQL database...')
#
#     def disconnect(self):
#         print('Disconnecting from PostgreSQL database...')
#
#     def execute(self, query):
#         print(f"Executing query '{query}' in PostgreSQL database...")
#

# ----------------------------------------------------------------------------------------------------------------------

# (10)




















