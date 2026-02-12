import sqlite3
import json
import mysql.connector
import os

from dotenv import load_dotenv
from character_types.warrior import Warrior
from character_types.mage import Mage
from character_types.archer import Archer
from character_types.healer import Healer
from character_types.shielder import Shielder
from models.account import Account


class AccountManager:
    _instance = None 

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(AccountManager, cls).__new__(cls)
        return cls._instance

    def __init__(self, db_name = "accounts.db"):
        if hasattr(self, 'initialized'):
            return None
        load_dotenv()
        self.conn = mysql.connector.connect(
           host=os.getenv("DB_HOST"),
           user=os.getenv("DB_USER"),
           password=os.getenv("DB_PASSWORD"),
           database=os.getenv("DB_NAME")
       )

        self.cursor = self.conn.cursor() # The Truck on the road
        self._create_table()
        self.initialized = True
        print(" [SYSTEM] Database Connection Established.")

    def _create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS accounts
                            (username VARCHAR(255) PRIMARY KEY NOT NULL,
                            salt TEXT NOT NULL,
                            password_hash TEXT NOT NULL,
                            difficulty TEXT NOT NULL,
                            main_character TEXT,
                            sub_character TEXT)''') # Define a load space 
        self.conn.commit() # Creating the load space

    def save_account(self, account):
        if not account or not isinstance(account, Account):
            raise ValueError("[ERROR] Invalid account object.")
        
        if not account.username:
            raise ValueError("[ERROR] Account must have a username.")

        try:
            main_char_json = json.dumps(account.main_character.to_dict()) if account.main_character else None
            sub_char_json = json.dumps(account.sub_character.to_dict()) if account.sub_character else None

            query = "INSERT INTO accounts VALUES (%s, %s, %s, %s, %s, %s)"
            data = (account.username, account.salt, account.password_hash, account.difficulty, main_char_json, sub_char_json)
            self.cursor.execute(query, data)
            self.conn.commit()
            return True
        except mysql.connector.IntegrityError:
            raise ValueError(f"Error: Username '{account.username}' is already taken.")
        except Exception as e:
            raise RuntimeError(f"Database Error: {e}")

    def load_account(self, username):
        if not username or not isinstance(username, str):
            raise ValueError("[ERROR] Invalid username.")

        try:
            query = "SELECT username, salt, password_hash, difficulty, main_character, sub_character FROM accounts WHERE username = %s"
            self.cursor.execute(query, (username, ))
            row = self.cursor.fetchone()

            if not row:
                raise ValueError(f"No account found with username '{username}'.")

            username, salt, password_hash, difficulty, main_character, sub_character = row
            loaded_account = Account.load_from_db(username, salt, password_hash, difficulty)

            loaded_account.main_character = self.load_character(main_character)
            loaded_account.sub_character = self.load_character(sub_character)

            return loaded_account
        
        except ValueError:
            raise 
        except Exception as e:
            raise RuntimeError(f"Error loading account: {e}")


    def load_character(self, json_str):
        if not json_str: 
            return None

        try:
            data = json.loads(json_str)
            char_type = data.get("type")
            char_name = data.get("name")
            
            if not char_type or not char_name:
                print(" [ERROR] Invalid character data: missing type or name.")
                return None

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
            else:
                 print(f" [WARNING] Unknown character type: {char_type}")

            # if character_type:
            #     character_type.hp = data.get("hp", 100)
            #     character_type.attack = data.get("attack", 10)
            #     character_type.stamina = data.get("stamina", 100)

            return character_type
            
        except json.JSONDecodeError:
            print(f" [ERROR] Failed to decode character JSON: {json_str}")
            return None
        except Exception as e:
            print(f" [ERROR] Error loading character: {e}")
            return None
            
    def close(self):
        try:
            if hasattr(self, 'cursor') and self.cursor:
                self.cursor.close()
                print(" [SYSTEM] DATABASE CURSOR CLOSED.")
        except Exception as e:
            print(f" [ERROR] FAILED TO CLOSE CURSOR: {e}")

        try:
            if hasattr(self, 'conn') and self.conn:
                self.conn.close()
                print(" [SYSTEM] DATABASE CONNECTION CLOSED.")
        except Exception as e:
            print(f" [ERROR] FAILED TO CLOSE CONNECTION: {e}")
        
        if hasattr(self, 'initialized'):
            del self.initialized
