from models.character import Character

class Mage(Character):
    BASE_HP = 80
    BASE_ATTACK = 40
    BASE_STAMINA = 30

    def __init__(self, name):
        super().__init__(name, hp=self.BASE_HP, attack=self.BASE_ATTACK, stamina=self.BASE_STAMINA)
        