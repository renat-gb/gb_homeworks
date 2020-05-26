from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def get_clothes(self):
        print("Main zone")


class Palto(Clothes):

    def __init__(self, val):
        self.palto_formula = (val / 6.5 + 0.5)

    @property
    def get_clothes(self):
        return self.palto_formula


class Suite(Clothes):

    def __init__(self, h):
        self.suit_formula = (2 * h + 0.3)

    @property
    def get_clothes(self):
        return self.suit_formula


palto = Palto(val=13)
print(palto.get_clothes)

suite = Suite(h=12)
print(suite.get_clothes)
