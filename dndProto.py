import itertools
from dice import d20, d12, d10, d8, d6, d4

print(d20.roll())

print(d10.roll())

class OrderedPair():
    
    def __init__(self):
        self.x = 0
        self.y = 0

    def __str__(self):
        return (f'({str(self.x)}, {str(self.y)})')
    

class Combatant():

    def __init__(self):
        self.health = None
        self.position = None
        self.armor_class = None

    def move(self):
        raise NotImplementedError

    def act(self):
        raise NotImplementedError

    #def _attack(attacker, victim):

    def _roll_attack(attacker, victim):
        
        #Roll d20, add modifiers, see if greater than enemy AC
    def _calculate_damage(attacker, victim):
    
    



class Player(Combatant):

    def __init__(self):
        super().__init__()
        self.position = OrderedPair()

    def move(self):
        self.position.x += int(input("How much do you want to move in the x? "))
        self.position.y += int(input("How much do you want to move in the ? "))

    def act(self):
        print(self.position)
        input("Act player!")




class Game():

    def play(self):
        player = Player()

        combatants = [player]

        for combatant in itertools.cycle(combatants):

            combatant.move()

            combatant.act()



game = Game()

game.play()


