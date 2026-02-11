import random
import os
import time
import json

from ui.color import Color as Col
from services.gameEngine import GameEngine
from models.enemyAccount import EnemyAccount


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
        cls.battle_info()
        while(True):
            cls.game_engine.reroll_stamina()
            cls.character_dashboard()
            cls.game_engine.user_turn()
            if cls.game_engine.is_game_over_2(): 
                cls.game_engine.end_game("user")
                break
            time.sleep(2)
            cls.character_dashboard()
            cls.game_engine.enemy_turn()
            if cls.game_engine.is_game_over_1(): 
                cls.game_engine.end_game("enemy")
                break
            time.sleep(2)

        cls.game_engine = None

    @classmethod
    def createAnemy(cls):
        name_list = []
        try:
            # Construct path to data/enemies.json
            # Assuming main.py is in root, and we are running from root.
            # But deeper reliability:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            file_path = os.path.join(base_dir, 'data', 'enemies.json')
            
            with open(file_path, 'r', encoding='utf-8') as file:
                name_list = json.load(file)
                
            if not name_list:
                raise ValueError("Enemy name list is empty.")
                
        except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
            print(f" [ERROR] Failed to load enemy names: {e}")
            # List if failed the data loading
            name_list = ['Goblin', 'Orc', 'Slime', 'Wolf', 'Bandit','Arathorn', 'Bladewing', 'Cyrus']

        enemyAccount = EnemyAccount()
        enemyAccount.create_main_character(random.choice(name_list))        
        enemyAccount.create_sub_character(random.choice(name_list))    

        return enemyAccount
        
    @classmethod
    def battle_info(cls):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Col.CYAN}╔{'═'*50}╗{Col.END}")
        print(f"{Col.CYAN}║{Col.END}{' '*50}{Col.CYAN}║{Col.END}")
        print(f"{Col.CYAN}║{Col.END} {Col.BOLD}{f'QUICK BATTEL BEGINS'.center(48)}{Col.END} {Col.CYAN}║{Col.END}")
        print(f"{Col.CYAN}║{Col.END}{' '*50}{Col.CYAN}║{Col.END}")
        print(f"{Col.CYAN}╚{'═'*50}╝{Col.END}")
        time.sleep(2)

    @classmethod
    def character_dashboard(cls):
        cls.battle_info()
        cls.game_engine.current_info()
        
        