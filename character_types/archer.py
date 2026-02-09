from models.character import Character

class Archer(Character):
    BASE_HP = 110
    BASE_ATTACK = 15
    BASE_STAMINA = 50

    def __init__(self, name):
        super().__init__(name, hp=self.BASE_HP, attack=self.BASE_ATTACK, stamina=self.BASE_STAMINA)
        
