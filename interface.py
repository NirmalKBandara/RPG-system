from account import Account 
#from character import Character
from character_types.warrior import Warrior
from character_types.mage import Mage
from character_types.archer import Archer
from character_types.healer import Healer
from character_types.shielder import Shielder


class Interface:
    @classmethod
    def game_menu(cls):
        print("="*30)
        print("Welcome To <Game name>")
        print("="*30)
        print("1. Create New Account")
        print("2. Login Account")
        print("3. About Game")
        print("4. Settings")
        print("5. Quit Game")
        print("-"*30)
        choise = cls.get_choise()
        if choise == "1":
            cls.new_account_menu()
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


    @classmethod
    def get_choise(cls):
        return input("Select an Option : ")

    @classmethod
    def get_username(cls):
        return input("Type your account name :")

    @classmethod
    def get_password(cls):
        return input("set your account password :") 

    @classmethod
    def new_account_menu(cls):
        print("="*30)
        username = cls.get_username()
        print("="*30)
        difficulty = cls.set_difficulty()
        print("="*30)
        account = Account.new_account(username, cls.get_password(), difficulty)
        print("="*30)
        print("Account Created Successfully !")
        print("="*30)
        cls.set_characters_menu()
        
        
    @classmethod
    def set_difficulty(cls):
        print("Set your difficulty : ")
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
            print("="*30)
            print("Invalid Option ! Try again...")
            return cls.set_difficulty()

    @classmethod
    def character_chose(cls, Character):
        print("Chsoe this one : ")
        print("1. Yes")
        print("2. No. Go back.")
        choise = cls.get_choise()
        if choise == "1":
            account.add_to_guild(Character)
            return None
        elif choise == "2":
            if Character in [Archer, Mage, Warrior]:
                return cls.set_main_character()
            elif Character in [Healer, Shielder]:
                return cls.set_sub_character()
        else:
            print("Invalid Option ! Try again...")
            return cls.character_chose()

    @classmethod
    def set_main_character(cls):
        print("Set your main character...")
        print("To see character infomation Chose a character : ")
        print("1. Warrior")
        print("2. Mage")
        print("3. Archer")
        choise = cls.get_choise()
        if choise == "1":
            Warrior.info()
            cls.character_chose(Warrior)
        elif choise == "2":
            Mage.info()
            cls.character_chose(Mage)
        elif choise == "3":
            Archer.info()
            cls.character_chose(Archer)
        else:
            print("="*30)
            print("Invalid Option ! Try again...")
            return cls.set_main_character()

    @classmethod
    def set_sub_character(cls):
        print("Set your sub character...")
        print("To see character infomation Chose a character : ")
        print("1. Healer")
        print("2. Shielder")
        choise = cls.get_choise()
        if choise == "1":
            Healer.info()
            cls.character_chose(Healer)
        elif choise == "2":
            Shielder.info()
            cls.character_chose(Shielder)
        else:
            print("="*30)
            print("Invalid Option ! Try again...")
            return cls.set_sub_character()

    @classmethod
    def set_characters_menu(cls):
        cls.set_main_character()
        cls.set_sub_character()

    #password = input("Set your account password :")