from character import Character

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, hp=80, attack=40, stamina=30)
        
    @staticmethod
    def info():
        print("-"*30)
        print("HP : 80")
        print("Attack : 40")
        print("Stamina : 30")
        print("-"*30)
        print("Low HP, High Attack, Medium Stamina")
