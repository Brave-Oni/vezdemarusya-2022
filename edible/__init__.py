import random


class Edible:
    food = [
        "груша",
        "яблоко",
        "яйцо",
        "сэндвич",
        "яичница",
        "бургер",
        "макароны",
        "печенюшка",
    ]

    not_food = [
        "персик",
        "пинг",
        "спаркс",
        "дигги",
        "авокадик",
        "зингер",
        "маруся",
        "безысходная бездная гнетущего бытия",
    ]

    def __init__(self):
        self.streak = 0

    def get_choices(self):
        lst = {random.choice(self.food), random.choice(self.not_food)}
        return lst

    def check(self, answer):
        if answer in self.food:
            self.streak += 1
        else:
            self.streak = 0

        return self.streak
