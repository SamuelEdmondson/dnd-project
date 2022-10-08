from enum import Enum, auto

class Weapon():

    def __init__(self, dice, cost, weight, type_, versatile=False, finesse=False, heavy=False, \
    reach=False, two_handed=False, special = False):
        self.dice = dice
        self.cost = cost
        self.weight = weight
        self.type_ = type_
        self.versatile = 

    def calculate_damage(damage=0, strength=0):

        total = modifier

        for die in dice:
            total += die.roll()

        return Damage(total, type_)

    class Properties():
        

class Damage():

    def __init__(self, quantity, type_):
        self.quantity = quantity
        self.type_ = enum()

    class Types(Enum):
        PIERCING = auto()
        BLUDGEONING = auto()
        SLASHING = auto()
        FIRE = auto()

club



#Longsword is versatile

#Slashing 1d8(1d10)








# battleaxe = Weapon(damage=2*[d10], cost=10, weight=10, type_=Damage.Types.PIERCING)

# battleaxe.calculate_damage(modifier=3) -> Damage(18, PIERCING)