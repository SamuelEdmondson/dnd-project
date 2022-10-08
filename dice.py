import random

class Dice():

    def __init__(self, sides):
        self.sides = sides

    def roll(self, modifier=0):
        return random.randint(1, self.sides) + modifier

d20 = Dice(sides=20)
d12 = Dice(sides=12)
d10 = Dice(sides=10)
d8 = Dice(sides=8)
d6 = Dice(sides=6)
d4 = Dice(sides=4)