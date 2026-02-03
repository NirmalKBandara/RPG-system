import random
from gameEngine import GameEngine
from enemyAccount import EnemyAccount
from account import Account

class QuickBattle:
    game_engine = None

    @classmethod
    def battleStart(cls, user_account):
        enemy_account = cls.createAnemy()
        cls.game_engine = GameEngine(
                user_account.main_character,
                user_account.sub_character,
                enemy_account.main_character,
                enemy_account.sub_character
                )
        #mode = user_account.difficulty
        while(True):
            game_engine.reroll_stamina()
            game_engine.user_turn()
            if game_engine.is_game_over_2(): 
                game_engine.end_game("user")
                break
            game_engine.enemy_turn()
            if game_engine.is_game_over_1(): 
                game_engine.end_game("enemy")
                break
            #enemy turn

        #remove game_engine object

    @classmethod
    def createAnemy(cls):
        try:
            with open('main_names.txt', 'r') as file:
                main_name_list = file.read().split('\n')
            with open('sub_names.txt', 'r') as file:
                sub_name_list = file.read().split('\n')
        except FileNotFoundError:
            print("ERROR !")   
        
        enemyAccount = EnemyAccount()

        enemyAccount.create_main_character(random.choice(main_name_list))        
        enemyAccount.create_sub_character(random.choice(sub_name_list))    

        return enemyAccount
        
