class Character:
    def __init__ (self, name, hp, attack, stamina):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.stamina = stamina
    
    def speak(self):
        print(f"{self.name} is ready for battle !" )

    