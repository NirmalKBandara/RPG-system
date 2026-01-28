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
        InterfaceLine.double_line()
        print("Welcome To <Game name>")
        InterfaceLine.double_line()
        print("1. Create New Account")
        print("2. Login Account")
        print("3. About Game")
        print("4. Settings")
        print("5. Quit Game")
        choise = cls.get_choise()
        if choise == "1":
            cls.new_account_menu()
            cls.game_menu()
        elif choise == "2":
            cls.login_menu()
            cls.game_menu()
        # elif choise == "3":
        #     cls.about_game()
        # elif choise == "4":
        #     cls.settings()
        # elif choise == "5":
        #     cls.quit_game()
        # else:
        #     print("Invalid Option ! Try again...")
        #     cls.game_menu()


    @classmethod
    def get_choise(cls):
        InterfaceLine.single_line()
        return input("Select an Option : ")

    @classmethod
    def get_username(cls):
        InterfaceLine.single_line()
        return input("Type your account name : ")

    @classmethod
    def get_password(cls):
        InterfaceLine.single_line()
        return input("set your account password : ") 

    @classmethod
    def new_account_menu(cls):
        username = cls.get_username()
        difficulty = cls.set_difficulty()
        cls.current_account = Account.new_account(username, cls.get_password(), difficulty)
        InterfaceLine.double_line()
        cls.set_characters_menu()
        if db_manager.save_account(current_account):
            print("Account saved to database successfully!")
        else:
            print("Failed to save account.")
        
        
    @classmethod
    def set_difficulty(cls):
        InterfaceLine.double_line()
        print("Set your difficulty")
        InterfaceLine.double_line()
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
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
        InterfaceLine.double_line()
        print("Chsoe this one : ")
        InterfaceLine.single_line()
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
        InterfaceLine.single_line()
        return input("Username : ")

    @classmethod
    def login_password(cls):
        InterfaceLine.single_line()
        return input("Username : ")

    @classmethod
    def login_menu(cls):
        cls.get_username()

    

    @classmethod
    def game_menu(cls):
        InterfaceLine.double_line()
        print("Welcome <acc name> to the <game>")
        InterfaceLine.double_line()
        print("1. Story Mode")
        print("2. Bounty Mode")
        print("3. Character Stats")
        print("4. Log Out Account")
        print("5. Quit Game")
        choise = cls.get_choise()
        # if choise == "1":
        #     cls.new_account_menu()
        # elif choise == "2":
        #     cls.login_menu()
        # elif choise == "3":
        #     cls.about_game()
        # elif choise == "4":
        #     cls.settings()
        # elif choise == "5":
        #     cls.quit_game()
        # else:
        #     print("Invalid Option ! Try again...")
        #     cls.game_menu()
    

    #password = input("Set your account password :")