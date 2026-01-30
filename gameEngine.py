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

    def enemy_turn(self, character3, character4)
        if character3.stamina < 6 and character4.stamina < 6:
            return Print("ENEMY PASS THEIR TURN.")
        else:    
            character = enemy_chosen_character(character3, character4)
            attack_type = chosen_attack(character)
            if attack_type == "P":
                return Print("ENEMY PASS THEIR TURN.")
            user_character = enemy_chosen_enemy(cls.character1, cls.character2)


        # print(f"ENEMY CHOSE {character.name} THE {type(character).__name__} TO ATTACK YOU.")
        # time.sleep(2)

    def enemy_chosen_enemy(self, character1, character2):
        character = [character1, character2][random.randint(0,1)]
        if self.can_chose_character(character):
            return character
        else:
            return self.enemy_chosen_enemy(character3, character4)   

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
            case 1: if character.stamina > 12: return "E" else return self.chosen_attack()
            case 2: if character.stamina > 18: return "Q" else return self.chosen_attack()
            case 3: return "P"


    #def start_game():

        # Battle start
        # After reroll both sides get stamina
        # User get to have a first try

    def process():

    def end_game():

    # Press N
    def normal_attack(self, character_x, character_y):
        if character_x.stamina < 6:
            print("LOW STAMINA ! CAN NOT PROFORM THIS ACTION.")
            return None
        character_y.hp -= character_x.attack        
        if character_y.hp <= 0 :
            #character_y dies

    # Press E
    def double_attack(self, character_x, character_y):
        if character_x.stamina < 12:
            print("LOW STAMINA ! CAN NOT PROFORM THIS ACTION.")
            return None
        
        character_y.hp -= character_x.attack*1.5 
        if character_y.hp <= 0 :
            #character_y dies

    # Press Q
    def heavy_attack(self, character_x, character_y):
        if character_x.stamina < 18:
            print("LOW STAMINA ! CAN NOT PROFORM THIS ACTION.")
            return None

        character_y.hp -= character_x.attack*2
        if character_y.hp <= 0 :
            #character_y dies