from character import Character

class Shielder(Character):
    def __init__(self, name):
        super().__init__(name, hp=85, attack=15, stamina=20)
        self.shield = 30
        
    @staticmethod
    def info():
        print("-"*30)
        print("HP : 85")
        print("Attack : 15")
        print("Stamina : 20")
        print("Shield : 30")
        print("-"*30)
        print("Medium HP, Medium Attack, Low Stamina and Have shielding ability.")