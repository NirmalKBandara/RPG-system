import sqlite3
import json
import mysql.connector

from character_types.warrior import Warrior
from character_types.mage import Mage
from character_types.archer import Archer
from character_types.healer import Healer
from character_types.shielder import Shielder
from account import Account


class AccountManager:
    _instance = None 

    def __new__(cls, *agr, **kwrags):
        if not cls._instance:
            cls._instance = super(AccountManager, cls).__new__(cls)
        return cls._instance

    def __init__(self, db_name = "accounts.db"):
        if hasattr(self, 'initialized'):
            return None

        self.conn = mysql.connector.connect(
           host="localhost",
           user="root",
           password="(Nirmal2003Bandara:",
           database="accounts"
       )

        self.cursor = self.conn.cursor() # The Truck on the road
        self._create_table()
        self.initialized = True
        print(" [SYSTEM] Database Connection Established.")

    def _create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS accounts
                            (username TEXT PRIMARY KEY,
                            salt TEXT NOT NULL,
                            password_hash TEXT NOT NULL,
                            difficulty TEXT NOT NULL,
                            main_character TEXT,
                            sub_character TEXT)''') # Define a load space 
        self.conn.commit() # Creating the load space

    def save_account(self, account):
        try:
            main_char_json = json.dumps(account.main_character.to_dict()) if account.main_character else None
            sub_char_json = json.dumps(account.sub_character.to_dict()) if account.sub_character else None

            query = "INSERT INTO accounts VALUES (%s, %s, %s, %s, %s, %s)"
            data = (account.username, account.salt, account.password_hash, account.difficulty, main_char_json, sub_char_json)
            self.cursor.execute(query, data)
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            print(f"Error !!! {account.username} is already taken")
            return False
        except Exception as e:
            print(f"Database Error: {e}")
            return False

    def load_account(self, username):
        try:
            query = "SELECT username, salt, password_hash, difficulty, main_character, sub_character FROM accounts WHERE username = ?"
            self.cursor.execute(query, (username, ))
            row = self.cursor.fetchone()

            if not row:
                print("No account found! Try again.")
                return None

            username, salt, password_hash, difficulty, main_character, sub_character = row
            loaded_account = Account.load_from_db(username, salt, password_hash, difficulty)

            loaded_account.main_character = Account.load_character(main_character)
            loaded_account.sub_character = Account.load_character(sub_character)

            return loaded_account
        
        except Exception as e:
            print(f"Error loading account: {e}")
            return None


    def load_character(self, json_str):
        if not json_str: 
            return None

        data = json.loads(json_str)
        char_type = data["type"]
        char_name = data["name"]

        character_type = None
        if char_type == "Warrior": 
            character_type = Warrior(char_name)
        elif char_type == "Mage": 
            character_type = Mage(char_name)
        elif char_type == "Archer": 
            character_type = Archer(char_name)
        elif char_type == "Healer": 
            character_type = Healer(char_name)
        elif char_type == "Shielder": 
            character_type = Shielder(char_name)

        if character_type:
            character_type.hp = data["hp"]
            character_type.attack = data["attack"]
            character_type.stamina = data["stamina"]

        return character_type
            
    def close(self):
        self.conn.close()
