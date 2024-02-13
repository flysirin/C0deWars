# По правилам локальных соревнований каждый прыжок оценивается пятью судьями, каждых из них должен выставить оценку - вещественное число от 0 до 10. Затем находиться среднее арифметическое по выставленным оценкам и умножается на коэффициент сложности прыжка, в результате получим значение балла спортсмена. Кто наберет самое большое количество баллов то и победит на этих соревнованиях.

# from dataclasses import dataclass, field
#
#
# @dataclass(order=True)
# class Athlet:
#     sort_index: float = field(init=False, repr=False)
#     name: str = field(compare=False)
#     coefficient: float = field(repr=False, compare=False)
#     scores: list = field(default_factory=list, repr=False, compare=False)
#
#     def __post_init__(self):
#         self.sort_index = (sum(self.scores) * self.coefficient) / len(self.scores)
#
#
# sportsmans = [
#     Athlet('Иван', 1.5, [9.0, 8.0, 7.0]),
#     Athlet('Петр', 1.0, [10.0, 9.0, 8.0]),
#     Athlet('Алексей', 1.2, [8.0, 7.0, 6.0])
# ]
#
# print(f"Победитель соревнований: {max(sportsmans)}")

# ----------------------------------------------------------------------------------------------------------------------

# (2)

# Ваша задача дописать класс Student так, чтобы в нем появились
# атрибут guid - уникальная случайно сгенерированная строка длиной 15 символов. Для этого воспользуйтесь заготовленной
# функций generate_guid. Атрибут не должен участвовать в инициализации и в методе __repr__
# поле email - строковое значение, которое назначает университет студенту. Формируется из имени и фамилии в нижнем
# регистре следующим образом {first_name}.{last_name}@uni.edu
# В инициализации не участвует
# поле tuition необязательный атрибут, обозначающий стоимость за обучение. По умолчанию студент учиться бесплатно,
# значит его tuition равно нулю. Для платников значение передается при инициализации. В __repr__ не участвует
# Также необходимо сортировать всех студентов сперва по стоимости обучения (кто учится бесплатно должны быть первыми),
# а затем по фамилии и имени.

# import random
# import string
# from dataclasses import dataclass, field
#
# alphabet = string.ascii_uppercase + string.digits
#
#
# def generate_guid():
#     guid = ''.join(random.choices(alphabet, k=15))
#     return guid
#
#
# @dataclass(order=True)
# class Student:
#     sort_index: tuple = field(init=False, repr=False)
#     guid: str = field(init=False, repr=False)
#     first_name: str
#     last_name: str
#     tuition: [int, float] = field(default=0, repr=False)
#     email: str = field(init=False)
#
#     def __post_init__(self):
#         self.guid = generate_guid()
#         self.email = f"{self.first_name.lower()}.{self.last_name.lower()}@uni.edu"
#         self.sort_index = self.tuition, self.last_name, self.first_name


# ----------------------------------------------------------------------------------------------------------------------

# (3)

# Создайте дата-класс Product, который хранит информацию о названии продукта и о его цене. При выводе товара должна
# отображаться только информация о его имени. Обязательно назовите name атрибут, который хранит название.
# Цену товара можете назвать как хотите
# Затем создайте класс продуктовой корзины Cart, в котором должна быть реализована возможность
# добавлять товары в корзины при помощи метода add_product. Добавляется один продукт за один вызов метода
# посчитать общую сумму содержащихся товаров в корзине при помощи метода get_total
# возможность применить скидку через apply_discount. Данный метод должен принимать размер скидки - целое число от 1 до 100,
# обозначающее % от цены, и сохраняет его в экземпляре класса. Если передать любое другое значение, то нужно вызывать исключение. Данный метод возвращать ничего не должен
# raise ValueError('Неправильное значение скидки')

# from dataclasses import dataclass, field
#
#
# @dataclass
# class Product:
#     name: str
#     price: [int, float] = field(repr=False)
#
#
# class Cart:
#     def __init__(self):
#         self.pieces = []
#         self.discount = 0
#
#     def add_product(self, product):
#         self.pieces.append(product)
#
#     def get_total(self):
#         return sum(i.price for i in self.pieces) * (1 - self.discount / 100)
#
#     def apply_discount(self, val: int):
#         if type(val) != int or not (1 <= val <= 100):
#             raise ValueError('Неправильное значение скидки')
#         self.discount = val


# ----------------------------------------------------------------------------------------------------------------------

# (4)

# Пришли сотрудники отдела продаж и решили добавить возможность работы продуктовой корзины с промокодами
#  Для этого нужно создать дата-класс Promo, который содержит код промокода и значение его скидки.
# Проверьте, чтобы значение скидки было целым числом и находилось в пределах от 1 до 100, обозначает % от цены.
# При всех остальных значениях будем считать, что промокод не дает скидку (как вариант,  можете указать, что значение
# скидки составляет 0)
# Далее вам понадобиться добавить метод apply_promo в классе Cart, который получает на вход код промокода и заведен
# ли в переменной ACTIVE_PROMO промокод с таким названием. Если существует, то необходимо применить его номинал к
# корзине товаров. Сам метод apply_promo ничего не возвращает, только печатает текст "Промокод <promo> успешно
# применился" или "Промокода <promo> не существует"
# А вот при вызове метода get_total должен учитываться промокод или скидка, если они были применены.
# Примечание: промокод нельзя использоваться вместе со скидкой. Используется последнее значение, которое применилось.

#
# from dataclasses import dataclass, field
#
#
# @dataclass
# class Product:
#     name: str
#     price: [int, float] = field(repr=False)
#
#
# @dataclass
# class Promo:
#     code: str
#     percent: [int, float] = 0
#
#
# class Cart:
#     def __init__(self):
#         self.pieces = []
#         self.discount = 0
#
#     def add_product(self, product):
#         self.pieces.append(product)
#
#     def get_total(self):
#         return sum(i.price for i in self.pieces) * (1 - self.discount / 100)
#
#     def apply_discount(self, val: int):
#         if type(val) != int or not (1 <= val <= 100):
#             raise ValueError('Неправильное значение скидки')
#         self.discount = val
#
#     def apply_promo(self, code):
#         for promo in ACTIVE_PROMO:
#             if code == promo.code:
#                 self.discount = promo.percent
#                 print(f"Промокод {code} успешно применился")
#                 return
#         print(f"Промокода {code} не существует")
#

# ----------------------------------------------------------------------------------------------------------------------

# (5)

# Сотрудники отдела продаж придумали новый тип промокода и хотят, чтобы вы его добавили. Идея его заключается в том,
# что он распространяется только на определенные товары в корзине.
# Для этого вам нужно доработать дата-класс Promo, чтобы он мог принимать список товаров, на который будет
# распространяться промокод. Если список товаров не передать при создании, то данный промокод применяется ко всей корзине целиком.
# Также необходимо доработать метод add_product в классе Cart. Необходимо добавить возможность передавать в него
# количество товара, которое добавляется в корзину. Например, строка
# cart.add_product(product1, 5)
# говорит о том, что нужно добавить в корзину 5 единиц товара product1. Если не передавать количество
# cart.add_product(product1)
# то нужно считать, что добавили одну единицу товара.
# Вся остальная реализация остается из предыдущего задания.


from dataclasses import dataclass, field


@dataclass
class Product:
    name: str
    price: [int, float] = field(repr=False)


@dataclass
class Promo:
    code: str
    percent: [int, float] = 0
    product: list = field(default=None)


class Cart:
    def __init__(self):
        self.products = []
        self.discount = 0
        self.promo_flag = False
        self.promo = None

    def add_product(self, product, count=1):
        for i in range(count):
            self.products.append(product)

    def get_total(self):
        if not self.promo_flag or not self.promo.product:
            return sum(i.price for i in self.products) * (1 - self.discount / 100)
        total_sum = 0
        for product in self.products:
            if product in self.promo.product:
                total_sum += product.price * (1 - self.discount / 100)
            else:
                total_sum += product.price
        return total_sum

    def apply_discount(self, val: int):
        if type(val) != int or not (1 <= val <= 100):
            raise ValueError('Неправильное значение скидки')
        self.promo_flag = False
        self.discount = val

    def apply_promo(self, code):
        for promo in ACTIVE_PROMO:
            if code == promo.code:
                self.discount = promo.percent
                self.promo_flag = True
                self.promo = promo
                print(f"Промокод {code} успешно применился")
                return
        print(f"Промокода {code} не существует")



book = Product('Книга', 100.0)
usb = Product('Флешка', 50.0)
pen = Product('Ручка', 10.0)

ACTIVE_PROMO = [
    Promo('new', 20, [pen]),
    Promo('all_goods', 30),
    Promo('sale', 50, [book, usb]),
]

cart = Cart()
cart.add_product(book, 10)
cart.add_product(pen)
cart.add_product(book, 5)
cart.add_product(usb, 5)
cart.add_product(usb, 15)
cart.add_product(pen, 2)

print(cart.get_total())

# Применение промокода в 50% на книги и флешки
cart.apply_promo('sale')
print(cart.get_total())  # 1280.0
