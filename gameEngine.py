import time

from character import Character 

class GameEngine:
    def __init__(character1, character2, character3, character4):
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
    def reroll_stamina(character1, character2, character3, character4):
        usesr_stamina_count = random.randint(10, 20)
        enemy_stamina_count = random.randint(6, 20)

        character1.add_stamina(usesr_stamina_count)
        character2.add_stamina(usesr_stamina_count)
        character3.add_stamina(enemy_stamina_count)
        character4.add_stamina(enemy_stamina_count)
    
    def user_turn(self, character1, character2):
        # What is the action you are going proform
        # Get user input N,E,Q, or P(for Pass the turn)
        if character1.stamina < 6 and character1.stamina < 6:
            print("DOESN'T HAVE ENOUGH STAMINA !")
            time.sleep(2)
            return Print("YOU HAVE TO PASS YOUR TURN") 
        else:
            print("CHOSE YOUR HERO TO ATTACK !")
            print(f"1. {character1.name} THE {type(character1).__name__}.")
            print(f"2. {character2.name} THE {type(character2).__name__}.")
            character = user_chosen_character(character3, character4, input("WHICH ONE YOU CHOSE IN THIS ROUND >"))
            attack_type = chosen_attack(character)
            if attack_type == "P":
                return Print("ENEMY PASS THEIR TURN.")
            
            print("WHO ARE YOU THINKING TO ATTACK !")
            print(f"1. {character3.name} THE {type(character3).__name__}.")
            print(f"2. {character4.name} THE {type(character4).__name__}.")
            enemy_character = user_chosen_enemy(cls.character3, cls.character4,  input("WHICH ONE YOU CHOSE IN THIS ROUND >"))
            # N, E, Q
            match attack_type:
                case "N":
                    self.normal_attack(character, enemy_character)
                    print(f"YOUR {type(character).__name__} USE NORMAL ATTACK !")
                case "E":
                    self.double_attack(character, enemy_character)
                    print(f"YOUR {type(character).__name__} USE DOUBLE ATTACK !")
                case "Q":
                    self.heavy_attack(character, enemy_character)
                    print(f"YOUR {type(character).__name__} USE HEAVY ATTACK !")
            return Print("NOW ITS ENEMY TURN.")

    def enemy_turn(self, character3, character4):
        if character3.stamina < 6 and character4.stamina < 6:
            print("DOESN'T HAVE ENOUGH STAMINA !")
            time.sleep(2)
            return Print("ENEMY PASS THEIR TURN.")
        else:    
            character = enemy_chosen_character(character3, character4)
            attack_type = chosen_attack(character)
            if attack_type == "P":
                return Print("ENEMY PASS THEIR TURN.")
            
            user_character = enemy_chosen_user(cls.character1, cls.character2)
            # N, E, Q
            match attack_type:
                case "N":
                    self.normal_attack(character, user_character)
                    print("ENEMY USE NORMAL ATTACK !")
                case "E":
                    self.double_attack(character, user_character)
                    print("ENEMY USE DOUBLE ATTACK !")
                case "Q":
                    self.heavy_attack(character, user_character)
                    print("ENEMY USE HEAVY ATTACK !")
            return Print("NOW ITS YOUR TURN.")

            
                                

        # print(f"ENEMY CHOSE {character.name} THE {type(character).__name__} TO ATTACK YOU.")
        # time.sleep(2)
    def is_alive(self, character):
        if character.hp > 0:
            return True
        else:
            return False
    
    def user_chosen_character(self, character1, character2, choise):
        character = [character1, character2][choise-1]
        if self.can_chose_character(character):
            return character
        else:
            print("YOU CAN NOT CHOSE THIS CHARACTER.")
            print("USE OTHER ONE.")
            return self.user_chosen_character(character1, character2, choise)

    def user_chosen_enemy(self, character1, character2):
        character = [character1, character2][choise-1]
        if self.is_alive(character):
            return character
        else:
            print("YOU CAN NOT ATTACK THIS CHARACTER.")
            print("USE OTHER ONE.")
            return self.user_chosen_enemy(character3, character4)  
    
    def enemy_chosen_user(self, character1, character2):
        character = [character1, character2][random.randint(0,1)]
        if self.is_alive(character):
            return character
        else:
            return self.enemy_chosen_user(character3, character4)   

    def enemy_chosen_character(self, character3, character4):
        character = [character3, character4][random.randint(0,1)]
        if self.can_chose_character(character):
            return character
        else:
            return self.enemy_chosen_character(character3, character4)
            
    def can_chose_character(self, character):
        if character.hp > 0:
            if character.stamina < 6:
                return False
            else:
                return True
        else: 
            return False

    def chosen_attack(self, character):
        match random.randint(0,3):
            case 0: return "N"
            case 1: 
                if character.stamina > 12: 
                    return "E" 
                else: 
                    return self.chosen_attack()
            case 2: 
                if character.stamina > 18: 
                    return "Q" 
                else: 
                    return self.chosen_attack()
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

    #def start_game():

        # Battle start
        # After reroll both sides get stamina
        # User get to have a first try

    #def process():

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