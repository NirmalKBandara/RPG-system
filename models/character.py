class Character:
    def __init__ (self, name, hp, attack, stamina):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.stamina = stamina
        self.shield = 0

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "name": self.name,
            "hp": self.hp,
            "attack": self.attack,
            "stamina": self.stamina
        }

    def zero_stamina(self):
        self.stamina = 0

    def add_stamina(self, amount):
        self.stamina += amount
    
    def reduce_stamina(self, attack_type):
        match attack_type:
            case "N":
                self.stamina -= 6
            case "E":
                self.stamina -= 12
            case "Q":
                self.stamina -= 18
            case "H":
                self.stamina -= 12
            case "S":
                self.stamina -= 12

    def shield(self, amount):
        self.shield = amount