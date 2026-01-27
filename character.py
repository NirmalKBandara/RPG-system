class Character:
    def __init__ (self, name, hp, attcak, stamina):
        self.name = name
        self.hp = hp
        self.attack = attcak
        self.stamina = stamina
    
    def speak(self):
        print(f"{self.name} is ready for battle !" )

    