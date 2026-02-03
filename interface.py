import sys
import os
import time
from color import Color as Col

from gameEngine import GameEngine
from account import Account 
from interfaceLine import InterfaceLine
from accountManager import AccountManager
#from character import Character
from character_types.warrior import Warrior
from character_types.mage import Mage
from character_types.archer import Archer
from character_types.healer import Healer
from character_types.shielder import Shielder

db_manager = AccountManager()

class Interface:
    current_account = None

    @classmethod
    def start_menu(cls):

        os.system('cls' if os.name == 'nt' else 'clear')

        print(f"{Col.CYAN}╔{'═'*50}╗{Col.END}")
        print(f"{Col.CYAN}║{Col.END}{' '*50}{Col.CYAN}║{Col.END}")
        print(f"{Col.CYAN}║{Col.END} {Col.BOLD}{f'WELCOME TO <Game name>'.center(48)}{Col.END} {Col.CYAN}║{Col.END}")
        print(f"{Col.CYAN}║{Col.END}{' '*50}{Col.CYAN}║{Col.END}")
        print(f"{Col.CYAN}╚{'═'*50}╝{Col.END}")
        
        print(f"\n   {Col.BOLD}LET'S GET STARTED!{Col.END}")
        print(f"\n   {Col.CYAN}[1]{Col.END} LOGIN ACCOUNT")
        print(f"   {Col.CYAN}[2]{Col.END} CREATE NEW ACCOUNT")
        print(f"   {Col.CYAN}[3]{Col.END} ABOUT GAME")
        print(f"   {Col.CYAN}[4]{Col.END} SETTINGS")
        print(f"   {Col.CYAN}[5]{Col.END} QUIT GAME")

        choise = cls.get_choise()
        if choise == "1":
            cls.login_menu()
            cls.game_menu()
        elif choise == "2":
            cls.new_account_menu()
            cls.game_menu()
        # elif choise == "3":
        #     cls.about_game()
        # elif choise == "4":
        #     cls.settings()
        elif choise == "5":
            print(5)
            sys.exit()
        # else:
        #     print("Invalid Option ! Try again...")
        #     cls.game_menu()


    @classmethod
    def get_choise(cls):
        print("")
        return input(f"{Col.YELLOW}SELECT AN OPTION > {Col.END}")

    @classmethod
    def get_username(cls):
        print("")
        return input(f"{Col.YELLOW}SET A USERNAME > {Col.END}")

    @classmethod
    def get_password(cls):
        print("")
        return input(f"{Col.YELLOW}SET A PASSWORD > {Col.END}") 

    @classmethod
    def new_account_menu(cls):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Col.CYAN}╔{'═'*50}╗{Col.END}")
        print(f"{Col.CYAN}║{Col.END}{' '*50}{Col.CYAN}║{Col.END}")
        print(f"{Col.CYAN}║{Col.END} {Col.BOLD}{f'CREATE NEW ACCOUNT'.center(48)}{Col.END} {Col.CYAN}║{Col.END}")
        print(f"{Col.CYAN}║{Col.END}{' '*50}{Col.CYAN}║{Col.END}")
        print(f"{Col.CYAN}╚{'═'*50}╝{Col.END}")
        username = cls.get_username()
        difficulty = cls.set_difficulty()
        cls.current_account = Account.new_account(username, cls.get_password(), difficulty)
        InterfaceLine.double_line()
        cls.set_characters_menu()
        if db_manager.save_account(cls.current_account):
            print("ACCOUNT SAVED TO DATABASE SUCCESSFULLY!")
        else:
            print("FAILED TO SAVE ACCOUNT.")
        
        
    @classmethod
    def set_difficulty(cls):

        print(f"\n{Col.CYAN}╔{'═'*50}╗{Col.END}")
        print(f"{Col.CYAN}║{Col.END}{' '*50}{Col.CYAN}║{Col.END}")
        print(f"{Col.CYAN}║{Col.END} {Col.BOLD}{f'SET DIFFICULTY'.center(48)}{Col.END} {Col.CYAN}║{Col.END}")
        print(f"{Col.CYAN}║{Col.END}{' '*50}{Col.CYAN}║{Col.END}")
        print(f"{Col.CYAN}╠{'═'*50}╣{Col.END}")
        
        print(f"{Col.CYAN}║{Col.END}{' '*50}{Col.CYAN}║{Col.END}")
        print(f"{Col.CYAN}║{Col.END}     {Col.GREEN}1. EASY{Col.END} {" "*(36)} {Col.CYAN}║{Col.END}")
        
        print(f"{Col.CYAN}║{Col.END}     {Col.YELLOW}2. MEDIUM{Col.END} {" "*(34)} {Col.CYAN}║{Col.END}")
        
        print(f"{Col.CYAN}║{Col.END}     {Col.RED}3. HARD{Col.END} {" "*(36)} {Col.CYAN}║{Col.END}")
        print(f"{Col.CYAN}║{Col.END}{' '*50}{Col.CYAN}║{Col.END}")
        print(f"{Col.CYAN}╚{'═'*50}╝{Col.END}")
        
        choise = cls.get_choise()
        if choise == "1":
            return "EASY"
        elif choise == "2":
            return "MEDIUM"
        elif choise == "3":
            return "HARD"
        else:
            print("INVALID OPTION ! TRY AGAIN...")
            print()
            time.sleep(2)
            return cls.set_difficulty()

    @classmethod
    def character_choise_menu(cls):
        print(f"\n   {Col.BOLD}ARE YOU SURE ?{Col.END}")
        print(f"   {Col.BOLD}NO GOING BACK AFTER SELECTION.{Col.END}")
        print(f"\n   {Col.CYAN}[1]{Col.END} YES.")
        print(f"   {Col.CYAN}[2]{Col.END} NO, GO BACK.")
    
    @classmethod
    def main_character_chose(cls, Character):
        cls.character_choise_menu()
        choise = cls.get_choise()
        if choise == "1":
            name = input(f"\n{Col.YELLOW}ENTER YOUR CHARACTER NAME > {Col.END}")
            cls.current_account.main_character = Character(name)
            return None
        elif choise == "2":
            cls.character_info()
            return cls.set_main_character()

    @classmethod
    def sub_character_chose(cls, Character):
        cls.character_choise_menu()
        choise = cls.get_choise()
        if choise == "1":

            name = input(f"\n{Col.YELLOW}ENTER YOUR CHARACTER NAME > {Col.END}")
            cls.current_account.sub_character = Character(name)
            return None
        elif choise == "2":
            cls.character_info()
            return cls.set_sub_character()
    
    @classmethod
    def character_info(cls):
        
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f"\n{Col.CYAN}╔{'═'*50}╗{Col.END}")
        print(f"{Col.CYAN}║{Col.END}{' '*50}{Col.CYAN}║{Col.END}")
        print(f"{Col.CYAN}║{Col.END} {Col.YELLOW}{Col.BOLD}{'CHARACTERS YOU CAN CHOOSE'.center(48)}{Col.END} {Col.CYAN}║{Col.END}")
        print(f"{Col.CYAN}║{Col.END}{' '*50}{Col.CYAN}║{Col.END}")
        print(f"{Col.CYAN}║{Col.END} {Col.YELLOW}{Col.BOLD}{'YOU CAN CHOOSE ONLY ONE CHARACTER FOR EACH ROLE'.center(48)}{Col.END} {Col.CYAN}║{Col.END}")
        print(f"{Col.CYAN}║{Col.END} {Col.YELLOW}{Col.BOLD}{'CHOOSE WISELY!'.center(48)}{Col.END} {Col.CYAN}║{Col.END}")
        print(f"{Col.CYAN}║{Col.END}{' '*50}{Col.CYAN}║{Col.END}")
        print(f"{Col.CYAN}╚{'═'*50}╝{Col.END}")

        # --- SECTION 1: MAIN CHARACTERS ---
        print(f"\n   {Col.RED}{Col.BOLD}MAIN CHARACTERS{Col.END}")
        print(f"   {Col.CYAN}{'━'*47}{Col.END}")
        print(f"   {Col.BOLD}{'CLASS':<12} {'HP':<6} {'ATK':<6} {'STA':<6} {'ABILITY':<15}{Col.END}")
        print(f"   {Col.CYAN}{'─'*47}{Col.END}")

        # Warrior
        print(f"   {Col.YELLOW}{'Warrior':<12}{Col.END} {str(Warrior.BASE_HP):<6} {str(Warrior.BASE_ATTACK):<6} {str(Warrior.BASE_STAMINA):<6} NONE")
        # Mage
        print(f"   {Col.YELLOW}{'Mage':<12}{Col.END} {str(Mage.BASE_HP):<6} {str(Mage.BASE_ATTACK):<6} {str(Mage.BASE_STAMINA):<6} NONE")
        # Archer
        print(f"   {Col.YELLOW}{'Archer':<12}{Col.END} {str(Archer.BASE_HP):<6} {str(Archer.BASE_ATTACK):<6} {str(Archer.BASE_STAMINA):<6} NONE")
        print(f"   {Col.CYAN}{'━'*47}{Col.END}")


        # --- SECTION 2: SUB CHARACTERS ---
        print(f"\n   {Col.GREEN}{Col.BOLD}SUB CHARACTERS {Col.END}")
        print(f"   {Col.CYAN}{'━'*47}{Col.END}")
        print(f"   {Col.BOLD}{'CLASS':<12} {'HP':<6} {'ATK':<6} {'STA':<6} {'ABILITY':<15}{Col.END}")
        print(f"   {Col.CYAN}{'─'*47}{Col.END}")

        # Healer
        print(f"   {Col.YELLOW}{'Healer':<12}{Col.END} {str(Healer.BASE_HP):<6} {str(Healer.BASE_ATTACK):<6} {str(Healer.BASE_STAMINA):<6} {Healer.ABILITY_NAME}: {Healer.ABILITY_VALUE}")
        # Shielder
        print(f"   {Col.YELLOW}{'Shielder':<12}{Col.END} {str(Shielder.BASE_HP):<6} {str(Shielder.BASE_ATTACK):<6} {str(Shielder.BASE_STAMINA):<6} {Shielder.ABILITY_NAME}: {Shielder.ABILITY_VALUE}")
        print(f"   {Col.CYAN}{'━'*47}{Col.END}")

    @classmethod
    def set_main_character(cls):
        print(f"\n{Col.CYAN}╔{'═'*50}╗{Col.END}")
        print(f"{Col.CYAN}║{Col.END} {Col.RED}{Col.BOLD}{'CHOOSE YOUR MAIN CHARACTER.'.center(48)}{Col.END} {Col.CYAN}║{Col.END}")
        print(f"{Col.CYAN}╚{'═'*50}╝{Col.END}")
        
        print(f"\n   {Col.BOLD}SELECT A CHARACTER:{Col.END}")
        
        print(f"\n   {Col.CYAN}[1]{Col.END} {Col.RED}WARRIOR{Col.END}")
        print(f"   {Col.CYAN}[2]{Col.END} {Col.PURPLE}MAGE   {Col.END}")
        print(f"   {Col.CYAN}[3]{Col.END} {Col.GREEN}ARCHER {Col.END}")

        print()
        choice = cls.get_choise()

        if choice == "1":
            cls.main_character_chose(Warrior)
        elif choice == "2":
            cls.main_character_chose(Mage)
        elif choice == "3":
            cls.main_character_chose(Archer)
        else:
            print(f"\n{Col.RED}INVALID OPTION! TRY AGAIN...{Col.END}")
            time.sleep(1)
            cls.character_info()
            return cls.set_main_character()

    @classmethod
    def set_sub_character(cls):
        cls.character_info()
        print(f"\n{Col.CYAN}╔{'═'*50}╗{Col.END}")
        print(f"{Col.CYAN}║{Col.END} {Col.RED}{Col.BOLD}{'CHOOSE YOUR SUB CHARACTER.'.center(48)}{Col.END} {Col.CYAN}║{Col.END}")
        print(f"{Col.CYAN}╚{'═'*50}╝{Col.END}")
        
        print(f"\n   {Col.BOLD}SELECT A CHARACTER:{Col.END}")
        
        print(f"\n   {Col.CYAN}[1]{Col.END} {Col.RED}HEALER{Col.END}")
        print(f"   {Col.CYAN}[2]{Col.END} {Col.PURPLE}SHIELDER   {Col.END}")

        choice = cls.get_choise()

        if choice == "1":
            cls.sub_character_chose(Healer)
        elif choice == "2":
            cls.sub_character_chose(Shielder)
        else:
            print(f"\n{Col.RED}INVALID OPTION! TRY AGAIN...{Col.END}")
            time.sleep(1)
            return cls.set_sub_character()


    @classmethod
    def set_characters_menu(cls):
        cls.character_info()
        cls.set_main_character()
        cls.set_sub_character()


    @classmethod
    def login_username(cls):
        print()
        cls.current_account = db_manager.load_account(input(f"{Col.YELLOW}ENTER THE USERNAME > {Col.END}"))
        if cls.current_account:
            return True
        else:
            return False 

    @classmethod
    def login_password(cls):
        print()
        if cls.current_account.check_password(input(f"{Col.YELLOW}ENTER THE PASSWORD > {Col.END}")):
            return True
        else:
            return False

    @classmethod
    def login_menu(cls):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Col.CYAN}╔{'═'*50}╗{Col.END}")
        print(f"{Col.CYAN}║{Col.END}{' '*50}{Col.CYAN}║{Col.END}")
        print(f"{Col.CYAN}║{Col.END} {Col.BOLD}{f'LOGIN PAGE'.center(48)}{Col.END} {Col.CYAN}║{Col.END}")
        print(f"{Col.CYAN}║{Col.END}{' '*50}{Col.CYAN}║{Col.END}")
        print(f"{Col.CYAN}╚{'═'*50}╝{Col.END}")
        if cls.login_username():
            if cls.login_password():
                print()
                print(f"{Col.CYAN} {Col.END} {Col.BOLD}{f'LOGIN SUCCESFULL !'.center(48)}{Col.END} {Col.CYAN} {Col.END}")
                time.sleep(2)
                print()
                print(f"{Col.CYAN} {Col.END} {Col.BOLD}{f'WELCOME {cls.current_account.username}.'.center(48)}{Col.END} {Col.CYAN} {Col.END}")
                time.sleep(2)
                cls.game_menu()
            else:
                print()
                print(f"{Col.CYAN} {Col.END} {Col.BOLD}{f'LOGIN UNSUCCESFULL !'.center(48)}{Col.END} {Col.CYAN} {Col.END}")
                time.sleep(2)
                return cls.login_menu()
        else:
            print()
            print(f"{Col.CYAN} {Col.END} {Col.BOLD}{f'LOGIN UNSUCCESFULL !'.center(48)}{Col.END} {Col.CYAN} {Col.END}")
            time.sleep(2)
            return cls.login_menu()
         

    @classmethod
    def game_menu(cls):
        # 1. Clear the screen (Makes it look like a new page)
        os.system('cls' if os.name == 'nt' else 'clear')

        acc = cls.current_account
        
        # 2. Get Character Info Safely
        m_name = acc.main_character.name if acc.main_character else "None"
        m_type = type(acc.main_character).__name__ if acc.main_character else ""
        
        s_name = acc.sub_character.name if acc.sub_character else "None"
        s_type = type(acc.sub_character).__name__ if acc.sub_character else ""

        # 3. Print the "Player Dashboard"
        print(f"\n{Col.CYAN}╔{'═'*50}╗{Col.END}")
        print(f"{Col.CYAN}║{Col.END}{' '*50}{Col.CYAN}║{Col.END}")
        print(f"{Col.CYAN}║{Col.END} {Col.BOLD}{f'ADVENTURER DASHBOARD: {acc.username.upper()}'.center(48)}{Col.END} {Col.CYAN}║{Col.END}")
        print(f"{Col.CYAN}║{Col.END}{' '*50}{Col.CYAN}║{Col.END}")
        print(f"{Col.CYAN}╠{'═'*50}╣{Col.END}")
        
        print(f"{Col.CYAN}║{Col.END}{' '*50}{Col.CYAN}║{Col.END}")
        # Difficulty Row
        print(f"{Col.CYAN}║{Col.END}  {Col.YELLOW}DIFFICULTY :{Col.END} {acc.difficulty.ljust(34)} {Col.CYAN}║{Col.END}")
        
        # Main Character Row
        m_display = f"{m_name} ({m_type})"
        print(f"{Col.CYAN}║{Col.END}  {Col.RED}MAIN HERO  :{Col.END} {m_display.ljust(34)} {Col.CYAN}║{Col.END}")
        
        # Sub Character Row
        s_display = f"{s_name} ({s_type})"
        print(f"{Col.CYAN}║{Col.END}  {Col.GREEN}SUPPORT    :{Col.END} {s_display.ljust(34)} {Col.CYAN}║{Col.END}")
        print(f"{Col.CYAN}║{Col.END}{' '*50}{Col.CYAN}║{Col.END}")
        print(f"{Col.CYAN}╚{'═'*50}╝{Col.END}")

        # 4. The Menu Options
        print(f"\n   {Col.BOLD}WHAT IS YOUR NEXT MOVE?{Col.END}")
        print(f"\n   {Col.CYAN}[1]{Col.END} STORY MODE")
        print(f"   {Col.CYAN}[2]{Col.END} QUICK BATTLE")
        print(f"   {Col.CYAN}[3]{Col.END} VIEW FULL STATS")
        print(f"   {Col.CYAN}[4]{Col.END} LOG OUT")
        print(f"   {Col.CYAN}[5]{Col.END} QUIT GAME")

        # 5. Get Input
        choice = cls.get_choise()
        if choice == '2':
            GameEngine
        # 6. Handle Logic (Same as before)
        elif choice == "4":
            print("LOGGING OUT...")
            cls.current_account = None
            cls.start_menu() # Go back to start
        elif choice == "5":
            print("GOODBYE!")
            exit()
        # elif choice == "3":
        #     cls.character_info()
        else:
             print("THIS FEATURE IS COMING SOON!")
             time.sleep(1)
             cls.game_menu()    
    

    #password = input("Set your account password :")