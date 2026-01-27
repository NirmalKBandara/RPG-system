from character import Character

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, hp=150, attack=25, stamina=20)
        
    @staticmethod
    def info():
        print("-"*30)
        print("HP : 150")
        print("Attack : 25")
        print("Stamina : 20")
        print("-"*30)
        print("High HP, Medium Attack, Low Stamina")




