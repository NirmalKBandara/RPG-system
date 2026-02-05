import time
import random
from color import Color as Col

from character import Character 

class GameEngine:
    def __init__(self, character1, character2, character3, character4):
        #user
        self.character1 = character1
        self.character2 = character2
        #enemy
        self.character3 = character3
        self.character4 = character4

        self.stamina_cap1 = character1.stamina
        self.character1_max_hp = character1.hp
        character1.zero_stamina()

        self.stamina_cap2 = character2.stamina
        self.character2_max_hp = character2.hp
        character2.zero_stamina()

        self.stamina_cap3 = character3.stamina
        self.character3_max_hp = character3.hp
        character3.zero_stamina()

        self.stamina_cap4 = character4.stamina
        self.character4_max_hp = character4.hp
        character4.zero_stamina()

    # easy mode
    def reroll_stamina(self):
        print("\nREROLL PHASE... ")
        time.sleep(1)
        self.character1.add_stamina(random.randint(0, 20))
        self.character2.add_stamina(random.randint(0, 20))
        self.character3.add_stamina(random.randint(6, 20))
        self.character4.add_stamina(random.randint(6, 20))
    
    def current_info(self):
        print("\n YOUR TEAM")
        print(f">>> {Col.BOLD}{self.character1.name}{Col.END} THE {Col.DARKCYAN}{type(self.character1).__name__}{Col.END} HAVE {Col.YELLOW}{self.character1.stamina}{Col.END} STAMINA AND {Col.GREEN}{self.character1.hp}{Col.END} HP.")
        print(f">>> {Col.BOLD}{self.character2.name}{Col.END} THE {Col.DARKCYAN}{type(self.character2).__name__}{Col.END} HAVE {Col.YELLOW}{self.character2.stamina}{Col.END} STAMINA AND {Col.GREEN}{self.character2.hp}{Col.END} HP.")

        print("\n ENEMY TEAM")
        print(f">>> {Col.BOLD}{self.character3.name}{Col.END} THE {Col.DARKCYAN}{type(self.character3).__name__}{Col.END} HAVE {Col.YELLOW}{self.character3.stamina}{Col.END} STAMINA AND {Col.GREEN}{self.character3.hp}{Col.END} HP.")
        print(f">>> {Col.BOLD}{self.character4.name}{Col.END} THE {Col.DARKCYAN}{type(self.character4).__name__}{Col.END} HAVE {Col.YELLOW}{self.character4.stamina}{Col.END} STAMINA AND {Col.GREEN}{self.character4.hp}{Col.END} HP.")


    def user_turn(self):
        # What is the action you are going proform
        # Get user input N,E,Q, or P(for Pass the turn)
        if self.character1.stamina < 6 and self.character2.stamina < 6:
            print("\n DOESN'T HAVE ENOUGH STAMINA !")
            time.sleep(2)
            return print("YOU HAVE TO PASS YOUR TURN") 
        else:
            print("\n CHOSE YOUR HERO TO ATTACK !")
            print(f"  1. {self.character1.name} THE {type(self.character1).__name__}.")
            print(f"  2. {self.character2.name} THE {type(self.character2).__name__}.")
            character = self.user_chosen_character(int(input("\n WHICH ONE YOU CHOSE IN THIS ROUND > ")))
            attack_type = self.user_chosen_attack(character)
            if attack_type == "P":
                return print("ENEMY PASS THEIR TURN.")
            
            print("\n WHO ARE YOU THINKING TO ATTACK !")
            print(f"1. {self.character3.name} THE {type(self.character3).__name__}.")
            print(f"2. {self.character4.name} THE {type(self.character4).__name__}.")
            enemy_character = self.user_chosen_enemy(int(input("\n  WHICH ONE YOU CHOSE IN THIS ROUND > ")))
            # N, E, Q
            match attack_type:
                case "N":
                    self.normal_attack(character, enemy_character)
                    print(f"\n YOUR {type(character).__name__} USE NORMAL ATTACK !")
                case "E":
                    self.double_attack(character, enemy_character)
                    print(f"\n YOUR {type(character).__name__} USE DOUBLE ATTACK !")
                case "Q":
                    self.heavy_attack(character, enemy_character)
                    print(f"\n YOUR {type(character).__name__} USE HEAVY ATTACK !")
            return print("\n NOW ITS ENEMY TURN.")

    def enemy_turn(self):
        if self.character3.stamina < 6 and self.character4.stamina < 6:
            print("\n DOESN'T HAVE ENOUGH STAMINA !")
            time.sleep(2)
            return print("\n ENEMY PASS THEIR TURN.")
        else:    
            character = self.enemy_chosen_character()
            attack_type = self.enemy_chosen_attack(character)
            if attack_type == "P":
                print("\n ENEMY PASS THEIR TURN.")
                return print("\n NOW ITS YOUR TURN.")
            
            user_character = self.enemy_chosen_user()
            # N, E, Q
            match attack_type:
                case "N":
                    self.normal_attack(character, user_character)
                    print("\n ENEMY USE NORMAL ATTACK !")
                case "E":
                    self.double_attack(character, user_character)
                    print("\n ENEMY USE DOUBLE ATTACK !")
                case "Q":
                    self.heavy_attack(character, user_character)
                    print("\n ENEMY USE HEAVY ATTACK !")
            return print("\n NOW ITS YOUR TURN.")

            
                                

        # print(f"ENEMY CHOSE {character.name} THE {type(character).__name__} TO ATTACK YOU.")
        # time.sleep(2)
    def is_alive(self, character):
        if character.hp > 0:
            return True
        else:
            return False
    
    def user_chosen_character(self, choise):
        character = [self.character1, self.character2][choise-1]
        if self.can_chose_character(character):
            return character
        else:
            print(" YOU CAN NOT CHOSE THIS CHARACTER.")
            print(" USE OTHER ONE.")
            return self.user_chosen_character(choise)

    def user_chosen_enemy(self, choise):
        character = [self.character3, self.character4][choise-1]
        if self.is_alive(character):
            return character
        else:
            print(" YOU CAN NOT ATTACK THIS CHARACTER.")
            print(" USE OTHER ONE.")
            return self.user_chosen_enemy(int(input(" WHICH ONE YOU CHOSE IN THIS ROUND >")))  
    
    def enemy_chosen_user(self):
        character = [self.character1, self.character2][random.randint(0,1)]
        if self.is_alive(character):
            return character
        else:
            return self.enemy_chosen_user()   

    def enemy_chosen_character(self):
        character = [self.character3, self.character4][random.randint(0,1)]
        if self.can_chose_character(character):
            return character
        else:
            return self.enemy_chosen_character()
            
    def can_chose_character(self, character):
        if character.hp > 0:
            if character.stamina < 6:
                return False
            else:
                return True
        else: 
            return False

    def user_chosen_attack(self, character):
        self.attack_type_info()
        match input("\n SELECT YOUR OPTION > "):
            case "N": return "N"
            case "E": 
                if character.stamina >= 12: 
                    return "E" 
                else:
                    print("INSUFFICIENT STAMINA...") 
                    return self.user_chosen_attack(character)
            case "Q": 
                if character.stamina >= 18: 
                    return "Q" 
                else:
                    print("INSUFFICIENT STAMINA...") 
                    return self.user_chosen_attack(character)
            case "P": return "P"

    def enemy_chosen_attack(self, character):
        match random.randint(0,3):
            case 0: return "N"
            case 1: 
                if character.stamina >= 12: 
                    return "E" 
                else: 
                    return self.enemy_chosen_attack(character)
            case 2: 
                if character.stamina >= 18: 
                    return "Q" 
                else: 
                    return self.enemy_chosen_attack(character)
            case 3: return "P"

    def is_game_over_1(self):
        if self.character1.hp > 0 or self.character2.hp > 0:
            return False
        else:
            return True

    def is_game_over_2(self):
        if self.character3.hp > 0 or self.character4.hp > 0:
            return False
        else:
            return True

    def end_game(self, winner):
        if winner == "user":
            print("CONGRADULATION ! YOU WON THE ROUND.")
            return print("KEEP IT UP.")
        if winner == "enemy":
            print("YOU LOSE THE ROUND.")
            return print("BETTER LUCK NEXT TIME.")
    # Press N
    def normal_attack(self, character_x, character_y):
        if character_x.stamina < 6:
            print("LOW STAMINA ! CAN NOT PROFORM THIS ACTION.")
            return None
        character_y.hp -= character_x.attack        
        if character_y.hp <= 0 :
            return #character_y dies

    # Press E
    def double_attack(self, character_x, character_y):
        if character_x.stamina < 12:
            print("LOW STAMINA ! CAN NOT PROFORM THIS ACTION.")
            return None
        
        character_y.hp -= character_x.attack*1.5 
        if character_y.hp <= 0 :
            return #character_y dies

    # Press Q
    def heavy_attack(self, character_x, character_y):
        if character_x.stamina < 18:
            print("LOW STAMINA ! CAN NOT PROFORM THIS ACTION.")
            return None

        character_y.hp -= character_x.attack*2
        if character_y.hp <= 0 :
            return #character_y dies
        
    def attack_type_info(self):
        print("\n N >>> | NORMAL ATTACK |  ATK*1  | STAMINA COST = 6  |")
        print(" E >>> | DOUBLE ATTACK | ATK*1.5 | STAMINA COST = 12 |")
        print(" Q >>> | HEAVY ATTACK  |  ATK*2  | STAMINA COST = 18 |")