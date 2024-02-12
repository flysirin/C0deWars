# По правилам локальных соревнований каждый прыжок оценивается пятью судьями, каждых из них должен выставить оценку - вещественное число от 0 до 10. Затем находиться среднее арифметическое по выставленным оценкам и умножается на коэффициент сложности прыжка, в результате получим значение балла спортсмена. Кто наберет самое большое количество баллов то и победит на этих соревнованиях.

from dataclasses import dataclass, field


@dataclass(order=True)
class Athlet:
    sort_index: float = field(init=False, repr=False)
    name: str = field(compare=False)
    coefficient: float = field(repr=False, compare=False)
    scores: list = field(default_factory=list, repr=False, compare=False)

    def __post_init__(self):
        self.sort_index = (sum(self.scores) * self.coefficient) / len(self.scores)


sportsmans = [
    Athlet('Иван', 1.5, [9.0, 8.0, 7.0]),
    Athlet('Петр', 1.0, [10.0, 9.0, 8.0]),
    Athlet('Алексей', 1.2, [8.0, 7.0, 6.0])
]

print(f"Победитель соревнований: {max(sportsmans)}")


# ----------------------------------------------------------------------------------------------------------------------

# (2)
