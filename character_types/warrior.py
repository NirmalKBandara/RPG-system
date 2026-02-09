from models.character import Character

class Warrior(Character):
    BASE_HP = 150
    BASE_ATTACK = 25
    BASE_STAMINA = 20

    def __init__(self, name):
        super().__init__(name, hp=self.BASE_HP, attack=self.BASE_ATTACK, stamina=self.BASE_STAMINA)
        



