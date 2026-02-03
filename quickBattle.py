import random
from gameEngine import GameEngine
from enemyAccount import EnemyAccount

class QuickBattle:
    gameEngine = None

    @classmethod
    def battleStart():
        while(True):
            #user turn

    @classmethod
    def createAnemy():
        nameList = ["Alice", "Bob", "Charlie", "David", "Eve"]
        
        enemyAccount = EnemyAccount()

        enemyAccount.create_main_character(random.choice(nameList))        
        enemyAccount.create_sub_character(random.choice(nameList))    
        
        Interface.main_character_chose(name1)
        character1 = []
        
