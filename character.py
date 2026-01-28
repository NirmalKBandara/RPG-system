class Character:
    def __init__ (self, name, hp, attack, stamina):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.stamina = stamina

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "name": self.name,
            "hp": self.hp,
            "attack": self.attack,
            "stamina": self.stamina
        }

    