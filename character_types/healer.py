from character import Character

class Healer(Character):
    def __init__(self, name):
        super().__init__(name, hp=100, attack=5, stamina=30)
        self.heal = 20
        
    @staticmethod
    def info():
        print("-"*30)
        print("HP : 100")
        print("Attack : 5")
        print("Stamina : 30")
        print("Heal : 20")
        print("-"*30)
        print("Medium HP, Low Attack, Medium Stamina and Have healing ability.")