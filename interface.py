import sys
import os
from color import Color as Col

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
        print(f"\n   {Col.CYAN}[1]{Col.END} Login Account")
        print(f"   {Col.CYAN}[2]{Col.END} Create New Account")
        print(f"   {Col.CYAN}[3]{Col.END} About Game")
        print(f"   {Col.CYAN}[4]{Col.END} Settings")
        print(f"   {Col.CYAN}[5]{Col.END} Quit Game")

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
        return input(f"{Col.YELLOW}Select an Option > {Col.END}")

    @classmethod
    def get_username(cls):
        print("")
        return input(f"{Col.YELLOW}Set a username > {Col.END}")

    @classmethod
    def get_password(cls):
        print("")
        return input(f"{Col.YELLOW}Set a password > {Col.END}") 

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
            print("Account saved to database successfully!")
        else:
            print("Failed to save account.")
        
        
    @classmethod
    def set_difficulty(cls):

        print(f"\n{Col.CYAN}╔{'═'*50}╗{Col.END}")
        print(f"{Col.CYAN}║{Col.END}{' '*50}{Col.CYAN}║{Col.END}")
        print(f"{Col.CYAN}║{Col.END} {Col.BOLD}{f'Set your difficulty'.center(48)}{Col.END} {Col.CYAN}║{Col.END}")
        print(f"{Col.CYAN}║{Col.END}{' '*50}{Col.CYAN}║{Col.END}")
        print(f"{Col.CYAN}╠{'═'*50}╣{Col.END}")
        
        print(f"{Col.CYAN}║{Col.END}{' '*50}{Col.CYAN}║{Col.END}")
        print(f"{Col.CYAN}║{Col.END}     {Col.GREEN}1. Easy{Col.END} {" "*(36)} {Col.CYAN}║{Col.END}")
        
        print(f"{Col.CYAN}║{Col.END}     {Col.YELLOW}2. Medium{Col.END} {" "*(34)} {Col.CYAN}║{Col.END}")
        
        print(f"{Col.CYAN}║{Col.END}     {Col.RED}3. Hard{Col.END} {" "*(36)} {Col.CYAN}║{Col.END}")
        print(f"{Col.CYAN}║{Col.END}{' '*50}{Col.CYAN}║{Col.END}")
        print(f"{Col.CYAN}╚{'═'*50}╝{Col.END}")
        
        choise = cls.get_choise()
        if choise == "1":
            return "Easy"
        elif choise == "2":
            return "Medium"
        elif choise == "3":
            return "Hard"
        else:
            InterfaceLine.double_line()
            print("Invalid Option ! Try again...")
            InterfaceLine.double_line()
            return cls.set_difficulty()

    @classmethod
    def character_choise_menu(cls):
        
        print("Chsoe this one : ")

        print("1. Yes")
        print("2. No. Go back.")
    
    @classmethod
    def main_character_chose(cls, Character):
        cls.character_choise_menu()
        choise = cls.get_choise()
        if choise == "1":
            name = input("Enter your character name : ")
            cls.current_account.main_character = Character(name)
            return None
        elif choise == "2":
            return cls.set_main_character()

    @classmethod
    def sub_character_chose(cls, Character):
        cls.character_choise_menu()
        choise = cls.get_choise()
        if choise == "1":
            name = input("Enter your character name : ")
            cls.current_account.sub_character = Character(name)
            return None
        elif choise == "2":
            return cls.set_sub_character()
    

    @classmethod
    def set_main_character(cls):
        InterfaceLine.double_line()
        print("Set your main character...")
        print("To see character infomation Chose a character : ")
        InterfaceLine.single_line()
        print("1. Warrior")
        print("2. Mage")
        print("3. Archer")
        choise = cls.get_choise()
        if choise == "1":
            Warrior.info()
            cls.main_character_chose(Warrior)
        elif choise == "2":
            Mage.info()
            cls.main_character_chose(Mage)
        elif choise == "3":
            Archer.info()
            cls.main_character_chose(Archer)
        else:
            InterfaceLine.double_line()
            print("Invalid Option ! Try again...")
            return cls.set_main_character()

    @classmethod
    def set_sub_character(cls):
        InterfaceLine.double_line()
        print("Set your sub character...")
        print("To see character infomation Chose a character : ")
        InterfaceLine.single_line()
        print("1. Healer")
        print("2. Shielder")
        choise = cls.get_choise()
        if choise == "1":
            Healer.info()
            cls.sub_character_chose(Healer)
        elif choise == "2":
            Shielder.info()
            cls.sub_character_chose(Shielder)
        else:
            InterfaceLine.double_line()
            print("Invalid Option ! Try again...")
            return cls.set_sub_character()


    @classmethod
    def set_characters_menu(cls):
        cls.set_main_character()
        cls.set_sub_character()


    @classmethod
    def login_username(cls):
        os.system('cls' if os.name == 'nt' else 'clear')

        cls.current_account = db_manager.load_account(input("Username : "))
        if cls.current_account:
            return True
        else:
            return False 

    @classmethod
    def login_password(cls):
        InterfaceLine.single_line()
        if cls.current_account.check_password(input("Password : ")):
            return True
        else:
            return False

    @classmethod
    def login_menu(cls):
        if cls.login_username():
            if cls.login_password():
                print("Login successful!")
                # print(cls.current_account.username)
                # print(cls.current_account.salt)
                # print(cls.current_account.password_hash)
                # print(cls.current_account.difficulty)
                # print(cls.current_account.main_character)
                # print(type(cls.current_account.main_character).__name__)
                # print(cls.current_account.sub_character)
                # print(type(cls.current_account.sub_character).__name__)
                cls.game_menu()
            else:
                print("Invalid password!")
                return cls.login_password()
        else:
            print("Invalid username!")
            return cls.login_username()
    
    # Search for username in the data base
    # if exists, get the account object
    # then cheack using account object's check_password mehtod 
         

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
        print(f"{Col.CYAN}║{Col.END}  {Col.YELLOW}Difficulty :{Col.END} {acc.difficulty.ljust(34)} {Col.CYAN}║{Col.END}")
        
        # Main Character Row
        m_display = f"{m_name} ({m_type})"
        print(f"{Col.CYAN}║{Col.END}  {Col.RED}Main Hero  :{Col.END} {m_display.ljust(34)} {Col.CYAN}║{Col.END}")
        
        # Sub Character Row
        s_display = f"{s_name} ({s_type})"
        print(f"{Col.CYAN}║{Col.END}  {Col.GREEN}Support    :{Col.END} {s_display.ljust(34)} {Col.CYAN}║{Col.END}")
        print(f"{Col.CYAN}║{Col.END}{' '*50}{Col.CYAN}║{Col.END}")
        print(f"{Col.CYAN}╚{'═'*50}╝{Col.END}")

        # 4. The Menu Options
        print(f"\n   {Col.BOLD}WHAT IS YOUR NEXT MOVE?{Col.END}")
        print(f"\n   {Col.CYAN}[1]{Col.END} Story Mode")
        print(f"   {Col.CYAN}[2]{Col.END} Bounty Mode")
        print(f"   {Col.CYAN}[3]{Col.END} View Full Stats")
        print(f"   {Col.CYAN}[4]{Col.END} Log Out")
        print(f"   {Col.CYAN}[5]{Col.END} Quit Game")

        # 5. Get Input
        choice = cls.get_choise()
        
        # 6. Handle Logic (Same as before)
        if choice == "4":
            print("Logging out...")
            cls.current_account = None
            cls.start_menu() # Go back to start
        elif choice == "5":
            print("Goodbye!")
            exit()
        else:
             print("This feature is coming soon!")
             input("Press Enter to continue...")
             cls.game_menu()    
    

    #password = input("Set your account password :")