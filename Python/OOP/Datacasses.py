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

import random
import string
from dataclasses import dataclass, field

alphabet = string.ascii_uppercase + string.digits


def generate_guid():
    guid = ''.join(random.choices(alphabet, k=15))
    return guid


@dataclass(order=True)
class Student:
    sort_index: tuple = field(init=False, repr=False)
    guid: str = field(init=False, repr=False)
    first_name: str
    last_name: str
    tuition: [int, float] = field(default=0, repr=False)
    email: str = field(init=False)

    def __post_init__(self):
        self.guid = generate_guid()
        self.email = f"{self.first_name.lower()}.{self.last_name.lower()}@uni.edu"
        self.sort_index = self.tuition, self.last_name, self.first_name

jane = Student('Jane', 'Lee')
julia = Student('Julia', 'Doe')
jake = Student('Jake', 'Langdon')
joy = Student('Joy', 'Smith')
print(*sorted([jane, julia, jake, joy]), sep='\n')
