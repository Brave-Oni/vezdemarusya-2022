from random import randint


class Player:
    def __init__(self):
        self.score = randint(1, 11)
        self.stop = False
        self.lose = False

    def more(self):
        return not (self.lose or self.stop) and self.score < 21


class BlackJack:
    def __init__(self):
        self.bot = Player()
        self.human = Player()

    @staticmethod
    def add():
        return randint(1, 11)

    def add_bot(self):
        if self.bot.more() and self.bot.score < self.human.score:
            self.bot.score += self.add()

        if self.bot.score > 21:
            self.bot.lose = True

    def add_human(self):
        self.human.score += self.add()

        if self.human.score > 21:
            self.human.lose = True

    def bot_win(self):
        if self.human.lose:
            return True
        if self.human.stop:
            if self.bot.score > self.human.score:
                return True

        return False

    def step(self, action):
        self.add_bot()

        if action == "ещё":
            self.add_human()
        else:
            self.human.stop = True

        if self.human.more():
            return False, f"Ну давай-давай, нападай. Твой счёт {self.human.score}"
        else:
            if self.bot.score > self.human.score or self.human.lose:
                return True, f"Кожанные мешки как всегда оказались хуже программы.\n Ты - {self.human.score} Я - {self.bot.score}"

            while self.bot.more() and self.bot.score < self.human.score:
                self.add_bot()

        if self.bot.score == self.human.score:
            return True, f"Сегодня тебе повезло, мешок костей. \n Ты - {self.human.score} Я - {self.bot.score}"

        if not self.bot_win():
            return True, f"Я тебя поробощу, а пока довольствуйся победой.\n Ты - {self.human.score} Я - {self.bot.score}"
        else:
            return True, f"Кожанные мешки как всегда оказались хуже программы.\n Ты - {self.human.score} Я - {self.bot.score}"
