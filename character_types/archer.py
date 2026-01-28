from character import Character

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, hp=110, attack=15, stamina=50)
        
    @staticmethod
    def info():
        print("-"*30)
        print("HP : 110")
        print("Attack : 15")
        print("Stamina : 50")
        print("-"*30)
        print("Medium HP, Low Attack, High Stamina")
