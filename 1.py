import random
import sys


class PlayLotto:
    def __init__(self, player_type):
        self.player = player_type
        self.card_generate()

    def card_generate(self):
        lst = [i for i in random.sample(range(1, 90), 15)]
        print(f" ---- Карточка {self.player} ----")
        print(sorted(lst[:5]))
        print(sorted(lst[5:10]))
        print(sorted(lst[10:15]))
        print("-" * 29)


class Bonk:
    def __init__(self, bonk_amount):
        self.bonk_amount = bonk_amount
        self.gen = self.bonk_start()

    def bonk_start(self):
        bonk_elements = [x for x in range(1, self.bonk_amount + 1)]
        random.shuffle(bonk_elements)
        # print(bonk_elements)

        for i, bonk_el in enumerate(bonk_elements):
            print(f"Бочонок номер {bonk_el}, ходов осталось: {self.bonk_amount - (i + 1)}")
            yield i


bonk = Bonk(90)
computer = PlayLotto(player_type="Computer")
human = PlayLotto(player_type="Human")

while True:
    num_bonk = next(bonk.gen)
    inp_data = input("Next? (y/n): ")
    if inp_data == "n":
        print("Game over!")
        sys.exit(1)
