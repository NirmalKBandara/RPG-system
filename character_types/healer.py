from character import Character

class Healer(Character):
    BASE_HP = 100
    BASE_ATTACK = 5
    BASE_STAMINA = 30
    ABILITY_NAME = "Heal"
    ABILITY_VALUE = 20

    def __init__(self, name):
        super().__init__(name, hp=self.BASE_HP, attack=self.BASE_ATTACK, stamina=self.BASE_STAMINA)
        self.heal = self.ABILITY_VALUE

    def get_ability(self):
        return self.ABILITY_VALUE