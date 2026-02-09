import random
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
                self.main_character = Warrior(name)
            case 1:
                self.main_character = Mage(name)
            case 2:
                self.main_character = Archer(name)

    def create_sub_character(self, name):
        match random.randint(0,1):
            case 0:
                self.sub_character = Healer(name)
            case 1:
                self.sub_character = Shielder(name)
    

    