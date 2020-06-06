import random
import sys


class PlayLotto:
    def __init__(self, player_type):
        self.player = player_type
        self.card_gen = self.card_generate()

    def card_generate(self):
        lst = [i for i in random.sample(range(1, 90), 15)]

        bonk_elements = [x for x in range(1, 90 + 1)]
        random.shuffle(bonk_elements)

        while True:
            lst_1 = sorted(lst[:5])
            lst_2 = sorted(lst[5:10])
            lst_3 = sorted(lst[10:15])

            return lst_1, lst_2, lst_3, self.player


class Bonk(PlayLotto):
    def bonk_start():
        bonk_elements = [x for x in random.sample(range(1, 90 + 1), 90)]

        print(bonk_elements[0])  # Элемент списка, который нужно сравнить

        for i, bonk_el in enumerate(bonk_elements):
            print(f"Бочонок номер {bonk_el}, ходов осталось: {90 - (i + 1)}")
            yield i


computer = PlayLotto(player_type="Computer")
human = PlayLotto(player_type="Human")

while True:
    print(computer.card_gen)
    print(human.card_gen)
    next(Bonk.bonk_start())

    inp_data = input("Next? (y/n): ")
    if inp_data == "n":
        print("Game over!")
        sys.exit(1)
