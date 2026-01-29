from character import Character

class Shielder(Character):
    BASE_HP = 85
    BASE_ATTACK = 15
    BASE_STAMINA = 20
    ABILITY_NAME = "Shield"
    ABILITY_VALUE = 30

    def __init__(self, name):
        super().__init__(name, hp=self.BASE_HP, attack=self.BASE_ATTACK, stamina=self.BASE_STAMINA)
        self.shield = self.ABILITY_VALUE
        