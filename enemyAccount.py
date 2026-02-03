from character_types.warrior import Warrior
from character_types.mage import Mage
from character_types.archer import Archer
from character_types.healer import Healer
from character_types.shielder import Shielder

class EnemyAccount:
    def __init__(self):
        self.main_character = None
        self.sub_character = None
        #self.guild = [] 

    def create_main_character(self, name):
        match random.randint(0,2):
            case 0:
                return Warrior(name)
            case 1:
                return Mage(name)
            case 2:
                return Archer(name)

    def create_sub_character(self, name):
        match random.randint(0,1):
            case 0:
                return Healer(name)
            case 1:
                return Shielder(name)
    

    